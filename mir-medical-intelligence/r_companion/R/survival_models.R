# Survival Analysis & Cox Proportional Hazards Helpers
library(survival)

fit_cox_model <- function(formula, data) {
  coxph(formula, data = data)
}
