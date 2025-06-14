library(tidyverse)
library(ggpubr)
library(rstatix)
library(lme4)
library(arm)
library(lattice)
library(effects)
library(sjPlot)
library(piecewiseSEM)

setwd('C:/Users/lenovo/Desktop/PhD/course regis/Comp Psycholing/data_for_R')

data <- read.csv(file = 'data_f_lexdec_w7s150.csv')

# mark categorical variables
data$isi=as.factor(data$isi)
data$prime=as.factor(data$prime)
data$target=as.factor(data$target)

modelLMER <- lmerTest::lmer(prim_diff_RT ~ diff_cosine # didn't include condition b/c it would highly correlate w/ cosine
                              + isi # control variable
                              + (1 | target) + (1 | prime), # prime/prime_un highly correlated
                              data = data)
summary(modelLMER)#how to save?

rsquared(modelLMER)

# assumption check (visually)
# 1. linearity - looks neat
linearity <- plot(resid(results),#extract the residuals
                         data$meanRT) #specify original y variable

# 2. normality of residuals & homoscedasticity - looks pretty good!
qqmath(results)
plot_model(results, type='diag')