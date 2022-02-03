extern "C" {
#include <stdlib.h>
#include <signal.h>
#include "ADS1263.h"
#include <inttypes.h>
#include <unistd.h>
};

#include <ifstream>
#include <iostream>
#include <vector>
#include <string>
#include "json.hpp"

#define REF	5.01
#define PORT 2000
#define MAXLINE 1024

string json_path = "";

int main(void)
{
	std::ifstream f(json_path);
	json j;
	f >> j;
	j = j["ADS1263"];

	double reference_voltage = r["reference voltage"];
    UDOUBLE raw_data[10];
	double voltage_data[10];
	double calibrated_data[10];

	ADS1263_SetMode(0);
	if(ADS1263_init_ADC1(ADS1263_38400SPS) == 1)
	{
		return 1;
	}

	while(1) {
		ADS1263_GetAll(raw_data);
		sprintf(data, "%" PRId64, now);
		fputs(data, log);
		for(i=0; i<10; i++) {
			if((ADC[i]>>31) == 1) {
				adc_data[i] = j["reference"]*2 - ADC[i]/2147483648.0 * j["reference"]; //7fffffff + 1
			}
			else {
				adc_data[i] = ADC[i]/2147483647.0 * j["reference"]; //7fffffff
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
}
