extern "C" {
#include <stdlib.h>
#include <signal.h>
#include "ADS1263.h"
#include <inttypes.h>
#include <unistd.h>
};

#include <iostream>
#include <vector>
#include <string>
#include <map>

#define REF			5.01		//Modify according to actual voltage
								//external AVDD and AVSS(Default), or internal 2.5V

#define PORT     2000
#define MAXLINE 1024

int main(void)
{
	char labels[10][100] = {
                         "pt0",
                         "pt1",
                         "pt2",
						 "pt3",
						 "pt4",
						 "pt5",
						 "pt6",
						 "pt7",
						 "pt8",
						 "pt9"
                     };
    UDOUBLE ADC[10];
	double adc_data[10];
	UWORD i;
	FILE *log;
	int sockfd;
	char log_dir[100] = "/home/ubuntu/logs/adc.csv";
	log = fopen(log_dir, "a+");
	int pipe = 0;
	char data[10000];

	ADS1263_SetMode(0);
	if(ADS1263_init_ADC1(ADS1263_38400SPS) == 1) {
		return 1;
	}

	uint64_t prev = millis() * 1000000;

	while(1) {
		uint64_t now = millis();
		ADS1263_GetAll(ADC);
		sprintf(data, "%" PRId64, now);
		fputs(data, log);
		for(i=0; i<10; i++) {
			if((ADC[i]>>31) == 1) {
				adc_data[i] = REF*2 - ADC[i]/2147483648.0 * REF; //7fffffff + 1
			}
			else {
				adc_data[i] = ADC[i]/2147483647.0 * REF; //7fffffff
			}
			if (pipe) {
				uint64_t nano_now = now * 1000000;
				int n = sprintf(data, "%s %s=%.5lf %" PRId64, labels[i], labels[i], adc_data[i], nano_now);
				std::cout << data << std::endl;
                                sendto(sockfd, data, n, 0, (struct sockaddr*)NULL, sizeof(servaddr));
			}
			sprintf(data, ",%.5lf", adc_data[i]);
			fputs(data, log);
		}
		data[0] = '\n';
		data[1] = '\0';
		fputs(data, log);
		pipe = 0;
	}
	return 0;
}
