#include <stdlib.h>
#include <stdio.h>

#include "splashhelper.h"

template <typename T>
int length(dynamic_array<T> &array)
{
  return array.size;
}

template <typename T>
void set_length(dynamic_array<T> &array, int size)
{
  array.size = size;
  T *new_data =  (T*) realloc(array.data, sizeof(T) * array.size);
  if (new_data)
  {
    array.data = new_data;
  }
  else
  {
    fprintf(stderr, "Out of memory");
    exit(EXIT_FAILURE);
  }
}

#include <string>
#include <iostream>

using namespace std;
using namespace std::string_literals;

#pragma mark string operator overloads

string operator + (string lhs, int rhs)
{
  return string(lhs + std::to_string(rhs));
  // return lhs;
}

string operator + (string lhs, long rhs)
{
  return string(lhs + std::to_string(rhs));
}

string operator + (string lhs, long long rhs)
{
  return lhs + std::to_string(rhs);
}

string operator + (string lhs, unsigned rhs)
{
  return lhs + std::to_string(rhs);
}

string operator + (string lhs, unsigned long rhs)
{
  return lhs + std::to_string(rhs);
}

string operator + (string lhs, unsigned long long rhs)
{
  return lhs + std::to_string(rhs);
}

string operator + (string lhs, float rhs)
{
  return lhs + std::to_string(rhs);
}

string operator + (string lhs, double rhs)
{
  return lhs + std::to_string(rhs);
}

string operator + (string lhs, long double rhs)
{
  return lhs + std::to_string(rhs);
}

#pragma mark Console Input

/**
 * Prints the provided message to the console
 * @param   message The message to print
 * @remarks         Prints without appending a newline character
 */
void print(const string message)
{
  std::cout << message;
}

void print(const int message)
{
  std::cout << message;
}

void print(const long message)
{
  std::cout << message;
}

void print(const long long message)
{
  std::cout << message;
}

void print(const unsigned message)
{
  std::cout << message;
}

void print(const unsigned long message)
{
  std::cout << message;
}

void print(const unsigned long long message)
{
  std::cout << message;
}

void print(const float message)
{
  std::cout << message;
}

void print(const double message)
{
  std::cout << message;
}

void print(const long double message)
{
  std::cout << message;
}

/**
 * Prints the provided message to the console and adds a new line
 * to the end of the string
 * @param   message The message to print
 * @remarks         Prints and appends a newline character
 */
void println(const string message)
{
  std::cout << message << std::endl;
}

void println(const int message)
{
  std::cout << message << std::endl;
}

void println(const long message)
{
  std::cout << message << std::endl;
}

void println(const long long message)
{
  std::cout << message << std::endl;
}

void println(const unsigned message)
{
  std::cout << message << std::endl;
}

void println(const unsigned long message)
{
  std::cout << message << std::endl;
}

void println(const unsigned long long message)
{
  std::cout << message << std::endl;
}

void println(const float message)
{
  std::cout << message << std::endl;
}

void println(const double message)
{
  std::cout << message << std::endl;
}

void println(const long double message)
{
  std::cout << message << std::endl;
}

/**
 * Reads a string in from the console
 * @return  The string the user entered
 */
string read_string()
{
  string result;
  // Stream from cin to result
  std::cin >> result;
  return result;
}

/**
 * Reads a string by first prompting the user with a prompt
 * @param  prompt The prompt to ask the user first before reading
 * @return        The string the user entered
 */
string read_string(const string prompt)
{
  print(prompt);
  return read_string();
}

// int main()
// {
//   dynamic_array<int> values;
//
//   // printf("Length: %d\n", length(values));
//
//   set_length<int>(values, 0);
//
//   // printf("values 0 = %d\n", values[0]);
//
//
//   printf("Length: %d\n", length(values));
//
//   set_length<int>(values, 5);
//   printf("Length: %d\n", length(values));
//
//   values[0] = 0;
//   values[1] = 1;
//   values[2] = 2;
//
//   printf("values 1 = %d\n", values[1]);
//   printf("values 10 = %d\n", values[10]);
//
//   return 0;
// }
