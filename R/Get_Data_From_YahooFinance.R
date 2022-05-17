######################################
# ---------- Yahoo Finance ----------#
######################################
# --- Loading library --- #
library(RCurl) # Allows data download from GitHub
library(quantmod)
# install.packages('quantmod') # It is recommended to install for optimal operation from "quantmod"

# --- Set data download start date --- #
date_day <- "2022-02-01"

# ---  A list with all the companies of interest is suggested --- #
gitpath <- getURL("https://raw.githubusercontent.com/juanmartinsantos/coding/main/SampleDatasets/companies.csv")
tb.comp <- read.csv(text = gitpath)
# tb.comp <- read.table("path/filename.csv") # To read a local file
symbs <- tb.comp$symbols # Get company symbols

# --- Create an empty dataframe to add the market data --- #
market <- data.frame()
col_names <- c("open", "high", "low", "close", "volume", "adjusted", "date", "symbol")

# --- Get market data from Yahoo Finance --- #
for(sym in 1:length(symbs)){
  mkt_aux <- data.frame(getSymbols(symbs[sym], src = "yahoo", from = date_day, to = Sys.Date(), auto.assign = FALSE))
  mkt_aux$date <- rownames(mkt_aux)
  rownames(mkt_aux) <- NULL
  mkt_aux$symbol <- symbs[sym]
  names(mkt_aux) <- col_names
  
  market <- rbind(market,mkt_aux)
  rm(mkt_aux)
}

# --- Don't forget to save your market data --- #
write.table(market, file = "path/filename")
