library(xlsx)
cus<-read.xlsx('cus.xlsx',sheetName = 'sheet')

# HIGHLIGHT

wb<- loadWorkbook('cus.xlsx')             
sheets <- getSheets(wb)
sheet <- sheets[['sheet']]

cs1<-CellStyle(wb)+Fill(
  #backgroundColor = '#FF0000',
  foregroundColor = 'red')
cs2<-CellStyle(wb)+Fill(
  foregroundColor = 'blue')
cs3<-CellStyle(wb)+Fill(
  foregroundColor = 'yellow')
cs4<-CellStyle(wb)+Fill(
  foregroundColor = '#550055')


date_row<-as.numeric(rownames(cus[which(cus$Update_Date==39860),]
                              ['Update_Date']))
date_row<-date_row+1
row1<-getRows(sheet,rowIndex = date_row)
cell1<-getCells(row1,colIndex = 12)
cell1
length(cell1)
lapply(names(cell1),
       function(ii)setCellStyle(cell1[[ii]],
                                cs4))


con1<-is.na(cus['Status'])
status_row1<-as.numeric(rownames(cus[which(con1),]
                                ['Status']))
status_row1<-status_row1+1
row2<-getRows(sheet,rowIndex = status_row1)
cell2<-getCells(row2,colIndex = 13)
cell2
length(cell2)
lapply(names(cell2),
       function(ii)setCellStyle(cell2[[ii]],
                                cs1))


sub<-subset(cus, Status=='Active'| Status=='Inactive')
status_row2<-as.numeric(rownames(sub['Status']))
status_row2<-status_row2+1
status_row2
row3<-getRows(sheet,rowIndex = status_row2)
cell3<-getCells(row3,colIndex = 13)
cell3
length(cell3)
lapply(names(cell3),
       function(ii)setCellStyle(cell3[[ii]],
                                cs2))


row4<-getRows(sheet,rowIndex = c(107,120,122))
cell4<-getCells(row4,colIndex = 14)
cell4
length(cell4)
lapply(names(cell4),
       function(ii)setCellStyle(cell4[[ii]],
                                cs3))

saveWorkbook(wb, 'cus.xlsx')

#CLEAN

#rownames(subset(cus,!con)['Phone'])
trim1<-gsub('Active','A',cus$Status)
cus$Status<-trim1
trim2<-gsub('Inactive','I',cus$Status)
cus$Status<-trim2
cus$Updated_by<-chartr('.','_',cus$Updated_by)

write.csv(cus,'cus.csv',row.names = FALSE)