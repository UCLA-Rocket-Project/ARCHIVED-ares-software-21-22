#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <iomanip>

int main()
{
    long start = 1643597400000;
    long end = 1643599200000;

    std::cout << std::fixed << std::setprecision(5);

    for(std::string line; std::getline(std::cin, line);)
    {
        std::stringstream line_stream(line);
        std::vector<double> values;
        while(line_stream.good())
        {
            std::string value;
            getline(line_stream, value, ','); //get first string delimited by comma
            values.push_back(std::stod(value));
        }
        cout << (long) values[0];

        if (values.size() > 0 && ((long) values[0]) >= start && ((long) values[0]) <= end)
        {
            for (std::vector<double>::iterator it = values.begin(); it != values.end(); ++it)
            {
                if (it == values.begin())
                {
                    std::cout << ((long) *it);
                }
                else
                {
                    std::cout << ',' << *it;
                }
            }
            std::cout << std::endl;
        }
    }
    return 0;
}