cmake_minimum_required(VERSION 3.16)
project(5j_c C)

set(CMAKE_C_STANDARD 99)

add_library(5j_c library.c library.h old_dice.c singou.c 2015tsukuba.c 2016tsukuba.c dice.c check.c 2017tsukuba1.c)