///
///
///
///

#define procedure void
#define main SK_main

#include <stdlib.h>
#include <string>
using namespace std;

void print(const string message);
void print(const int message);
void print(const long message);
void print(const long long message);
void print(const unsigned message);
void print(const unsigned long message);
void print(const unsigned long long message);
void print(const float message);
void print(const double message);
void print(const long double message);

void println(const string message);
void println(const int message);
void println(const long message);
void println(const long long message);
void println(const unsigned message);
void println(const unsigned long message);
void println(const unsigned long long message);
void println(const float message);
void println(const double message);
void println(const long double message);

string read_string();
string read_string(const string prompt);

///
/// A dynamic_array allows you to easily create an array whos length can change
/// dynamically. To check the current length, call the length function. To
/// change the length, call the set_length<T> function.
///
template <typename T>
struct dynamic_array
{
  T *data;
  unsigned int size;

  dynamic_array()
  {
    data = NULL;
    size = 0;
  }

  T& operator[] (const int index)
  {
    if ( index >= size )
    {
      fprintf(stderr, "Accessing dynamic array past bounds.");
      if ( size > 0 )
        fprintf(stderr, " Accessed index %d, valid indexes are 0..%d.\n", index, size - 1);
      else
        fprintf(stderr, " Accessed empty dynamic array.\n");
      exit(EXIT_FAILURE);
    }
    return data[index];
  }
};

template <typename T>
int length(dynamic_array<T> &array);

template <typename T>
void set_length(dynamic_array<T> &array);
