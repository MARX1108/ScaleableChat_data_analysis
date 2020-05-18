#clear the variable in the history
library(rjson)
rm(list=ls())
setwd("/Users/marxwang/Desktop/CODE/R/MutiThread/python")  ## set the working directory
study4 = read.csv("4.csv", header = TRUE) 
study5 = read.csv("5.csv", header = TRUE) 
study6 = read.csv("6.csv", header = TRUE) 
study7 = read.csv("7.csv", header = TRUE) 
study8 = read.csv("8.csv", header = TRUE) 
study9 = read.csv("9.csv", header = TRUE) 

library(tibble)

index <- seq(from = 4, to = 4, length.out = nrow(study4))
study4$index <- index
add_column(study4, index, .before = 'X')

