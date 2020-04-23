# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 11:11:54 2017

@author: Menna.tarek
"""


from plotly.offline import  init_notebook_mode, plot
import plotly.graph_objs as go
import pandas as pd
import datetime
datetime.datetime.strptime
from dateutil import parser



''' DRAW FUNCTION '''







'''function reading data from excel sheet adding it to a dictionary each one of them is a separate file '''
def readData(path):
   parse_date = lambda x: x.strftime('%Y/%m/%d')
   xls = pd.ExcelFile(path)
   stocks={}
   for sh in xls.sheet_names:
       stocks[sh]=pd.read_excel(xls,sh, index_col=None, na_values=['NA'] , converters={'Date (GMT)':parse_date})
   return stocks



''' Function to calculate total volume over a day and total turn over '''
def indexVsVol(Index,volume):
    
    indexVsVol = pd.DataFrame(Index['Date (GMT)'])
    indexVsVol = pd.concat([indexVsVol,Index['Last']],axis=1)  

    
    ''' saving volume sumition over the whole period '''
    oldDate = volume.get_value(0, 'Date', takeable=False)
    newDate = volume.get_value(0, 'Date', takeable=False)
    
    '''preparing volume '''
    volsum = 0.0
    volume['volumeSum'] = 0.0
    
    '''preparing TurnOver '''
    totalturnover = 0.0
    volume['totalTurnOver'] = 0.0
    
    ''' preparing ''' 
    totalretailvolume = 0.0 
    totalretailturnover = 0.0
    volume['totalRetailsVolume'] = 0.0
    volume['totalRetailsTurnOver'] = 0.0
    totalinistitutesvolume = 0.0
    totalinistitutesturnover = 0.0
    volume['totalInistitutesVolume'] = 0.0
    volume['totalInistitutesTurnOver'] = 0.0
    
    
    
    totalforeignersvolume = 0.0
    volume['totalForeignersVolume'] = 0.0
    totalforeignersturnover = 0.0
    volume['totalForeignersTurnOver'] = 0.0
    
    totalarabsvolume = 0.0
    volume['totalArabsVolume'] = 0.0
    totalarabsturnover = 0.0
    volume['totalArabsTurnOver'] = 0.0
    
    totalegyptionsvolume = 0.0
    volume['totalEgyptionsVolume'] = 0.0
    totalegyptionsturnover = 0.0
    volume['totalEgyptionsTurnOver'] = 0.0
    
    
          
          
    '''indicators'''
    retailbuyer = 0.0
    retailseller = 0.0
    retailbuyerorseller = 0.0
    volume['retailBuyerOrSeller'] = 0.0
          
    
    institutesbuyer = 0.0
    institutesseller = 0.0
    institutesbuyerorseller = 0.0
    volume['institutesBuyerOrSeller'] = 0.0
          
          
    foreignerbuyer = 0.0
    foreignerseller = 0.0
    foreignerbuyerorseller = 0.0
    volume['foreignerBuyerOrSeller'] = 0.0
   
    arabbuyer = 0.0
    arabseller = 0.0
    arabbuyerorseller = 0.0
    volume['arabBuyerOrSeller'] = 0.0 
    
    egyptionbuyer = 0.0
    egyptionseller = 0.0
    egyptionbuyerorseller = 0.0
    volume['egyptionBuyerOrSeller'] = 0.0 
         
          
          
    i = 0

    
    for index,row in volume.iterrows():
        institutesbuyerorseller = 0.0
        
        newDate = row['Date']
        
        ''' For Last Row '''
        if(index==(len(volume)-1)):
            
            
            
            ''' sitting summation of volume and  '''

            volsum = volsum + row['Volume']
            totalturnover = totalturnover + row['TurnOver']
            
            ''' retail '''
            if (volume.get_value(index, 'Type', takeable=False)) == "Retail":
                totalretailvolume = totalretailvolume + row['Volume']
                totalretailturnover = totalretailturnover + row['TurnOver']
                
                ''' BUYER OR SELLER '''
                if (row['Trans'] == 'Buy'):
                    retailbuyer = retailbuyer + row['Volume']
                else:
                    retailseller = retailseller + row['Volume']
                    
                
                
                
                ''' inistitutes '''
            else:
                totalinistitutesvolume = totalinistitutesvolume + row['Volume']
                totalinistitutesturnover = totalinistitutesturnover + row['TurnOver']
                
                ''' BUYER OR SELLER '''
                if (row['Trans'] == 'Buy'):
                    institutesbuyer = institutesbuyer + row['Volume']
                else:
                    institutesseller = institutesseller + row['Volume']
                
                
                '''Foreigners'''
            if(volume.get_value(index, 'Investor', takeable=False)) == "Foreigners":
                totalforeignersvolume = totalforeignersvolume + row['Volume']
                totalforeignersturnover = totalforeignersturnover + row['TurnOver']
                
                
                ''' BUYER OR SELLER '''
                if (row['Trans'] == 'Buy'):
                    foreignerbuyer = foreignerbuyer + row['Volume']
                else:
                    foreignerseller = foreignerseller + row['Volume']
                
                
                ''' arabs '''
            elif(volume.get_value(index, 'Investor', takeable=False)) == "Arabs":
                totalarabsvolume = totalarabsvolume + row['Volume']
                totalarabsturnover = totalarabsturnover + row['TurnOver']
                
                ''' BUYER OR SELLER '''
                if (row['Trans'] == 'Buy'):
                    arabbuyer = arabbuyer + row['Volume']
                else:
                    arabseller = arabseller + row['Volume']
                
                
                ''' egyptions '''
            else:
                totalegyptionsvolume = totalegyptionsvolume + row['Volume']
                totalegyptionsturnover = totalegyptionsturnover + row['TurnOver']
                
                
                ''' BUYER OR SELLER '''
                if (row['Trans'] == 'Buy'):
                    egyptionbuyer = egyptionbuyer + row['Volume']
                else:
                    egyptionseller = egyptionseller + row['Volume']
            
            
            
            ''' Total Volume '''
            volsum = float(volsum)/2
            volume.set_value(i, 'volumeSum', volsum)
            
            ''' Total TurnOver '''
            totalturnover = float(totalturnover)/2
            volume.set_value(i, 'totalTurnOver', totalturnover)
            
            
            ''' Total Retail & institutes Volume '''
            totalretailvolume = float(totalretailvolume)/2
            totalretailvolume = totalretailvolume/volsum
                         
            totalinistitutesvolume = float(totalinistitutesvolume)/2                             
            totalinistitutesvolume = totalinistitutesvolume/volsum
                              
            volume.set_value(i, 'totalRetailsVolume', totalretailvolume)
            volume.set_value(i, 'totalInistitutesVolume', totalinistitutesvolume)
            
            ''' Total Retail & institutes TurnOver '''
            totalretailturnover = float(totalretailturnover)/2
            totalretailturnover = totalretailturnover/totalturnover
                           
            totalinistitutesturnover = float(totalinistitutesturnover)/2
            totalinistitutesturnover = totalinistitutesturnover/totalturnover
                                
            volume.set_value(i, 'totalRetailsTurnOver', totalretailturnover)
            volume.set_value(i, 'totalInistitutesTurnOver', totalinistitutesturnover)
            
            ''' Total investors type volume '''
            totalforeignersvolume = float(totalforeignersvolume)/2
            totalforeignersvolume = totalforeignersvolume/volsum
                             
            totalarabsvolume = float(totalarabsvolume)/2
            totalarabsvolume = totalarabsvolume/volsum                    
            totalegyptionsvolume = float(totalegyptionsvolume)/2
            totalegyptionsvolume = totalegyptionsvolume/volsum
            
            volume.set_value(i, 'totalForeignersVolume', totalforeignersvolume)
            volume.set_value(i, 'totalArabsVolume', totalarabsvolume)
            volume.set_value(i, 'totalEgyptionsVolume', totalegyptionsvolume)
            
 
            ''' Total investors type turnover '''
            totalforeignersturnover = float(totalforeignersturnover)/2
            totalforeignersturnover = totalforeignersturnover/totalturnover                               
            totalarabsturnover= float(totalarabsturnover)/2
            totalarabsturnover = totalarabsturnover/totalturnover                         
            totalegyptionsturnover = float(totalegyptionsturnover)/2
            totalegyptionsturnover = totalegyptionsturnover/totalturnover
            
            volume.set_value(i, 'totalForeignersTurnOver', totalforeignersturnover)
            volume.set_value(i, 'totalArabsTurnOver', totalarabsturnover)
            volume.set_value(i, 'totalEgyptionsTurnOver', totalegyptionsturnover)
            
            
            ''' BUYER OR SELLER '''
            retailbuyerorseller = retailbuyer - retailseller
            volume.set_value(i, 'retailBuyerOrSeller', retailbuyerorseller)

            institutesbuyerorseller = institutesbuyer - institutesseller
            volume.set_value(i, 'institutesBuyerOrSeller', institutesbuyerorseller)
            
            
            
            foreignerbuyerorseller = foreignerbuyer -foreignerseller
            volume.set_value(i, 'foreignerBuyerOrSeller', foreignerbuyerorseller)
            
            arabbuyerorseller = arabbuyer -arabseller
            volume.set_value(i, 'arabBuyerOrSeller', arabbuyerorseller)
            
            egyptionbuyerorseller = egyptionbuyer -egyptionseller
            volume.set_value(i, 'egyptionBuyerOrSeller', egyptionbuyerorseller)
            

                
                
        elif (oldDate == newDate):
            ''' sitting summation of volume and  '''

            volsum = volsum + row['Volume']
            totalturnover = totalturnover + row['TurnOver']
            
            
            ''' retail '''
            if (volume.get_value(index, 'Type', takeable=False)) == "Retail":
                totalretailvolume = totalretailvolume + row['Volume']
                totalretailturnover = totalretailturnover + row['TurnOver']
                
                ''' BUYER OR SELLER '''
                if (row['Trans'] == 'Buy'):
                    retailbuyer = retailbuyer + row['Volume']
                else:
                    retailseller = retailseller + row['Volume']
                    
                
                
                
                ''' inistitutes '''
            else:
                
                totalinistitutesvolume = totalinistitutesvolume + row['Volume']
                totalinistitutesturnover = totalinistitutesturnover + row['TurnOver']

                ''' BUYER OR SELLER '''
                if (row['Trans'] == 'Buy'):
                    institutesbuyer = institutesbuyer + row['Volume']
                else:
                    institutesseller = institutesseller + row['Volume']
                
                
                '''Foreigners'''
            if(volume.get_value(index, 'Investor', takeable=False)) == "Foreigners":
                totalforeignersvolume = totalforeignersvolume + row['Volume']
                totalforeignersturnover = totalforeignersturnover + row['TurnOver']
                
                
                ''' BUYER OR SELLER '''
                if (row['Trans'] == 'Buy'):
                    foreignerbuyer = foreignerbuyer + row['Volume']
                else:
                    foreignerseller = foreignerseller + row['Volume']
                
                
                ''' arabs '''
            elif(volume.get_value(index, 'Investor', takeable=False)) == "Arabs":
                totalarabsvolume = totalarabsvolume + row['Volume']
                totalarabsturnover = totalarabsturnover + row['TurnOver']
                
                ''' BUYER OR SELLER '''
                if (row['Trans'] == 'Buy'):
                    arabbuyer = arabbuyer + row['Volume']
                else:
                    arabseller = arabseller + row['Volume']
                
                
                ''' egyptions '''
            else:
                totalegyptionsvolume = totalegyptionsvolume + row['Volume']
                totalegyptionsturnover = totalegyptionsturnover + row['TurnOver']
                
                
                ''' BUYER OR SELLER '''
                if (row['Trans'] == 'Buy'):
                    egyptionbuyer = egyptionbuyer + row['Volume']
                else:
                    egyptionseller = egyptionseller + row['Volume']
        
        else: 
            ''' Total Volume '''
            
            volsum = float(volsum)/2
            volume.set_value(i, 'volumeSum', volsum)
            
            ''' Total TurnOver '''
            totalturnover = float(totalturnover)/2
            volume.set_value(i, 'totalTurnOver', totalturnover)
            
            
            ''' Total Retail & institutes Volume '''
            totalretailvolume = float(totalretailvolume)/2
            totalretailvolume = totalretailvolume/volsum
                         
            totalinistitutesvolume = float(totalinistitutesvolume)/2                             
            totalinistitutesvolume = totalinistitutesvolume/volsum
                              
            volume.set_value(i, 'totalRetailsVolume', totalretailvolume)
            volume.set_value(i, 'totalInistitutesVolume', totalinistitutesvolume)
            
            ''' Total Retail & institutes TurnOver '''
            totalretailturnover = float(totalretailturnover)/2
            totalretailturnover = totalretailturnover/totalturnover
                           
            totalinistitutesturnover = float(totalinistitutesturnover)/2
            totalinistitutesturnover = totalinistitutesturnover/totalturnover
                                
            volume.set_value(i, 'totalRetailsTurnOver', totalretailturnover)
            volume.set_value(i, 'totalInistitutesTurnOver', totalinistitutesturnover)
            
            ''' Total investors type volume '''
            totalforeignersvolume = float(totalforeignersvolume)/2
            totalforeignersvolume = totalforeignersvolume/volsum
                             
            totalarabsvolume = float(totalarabsvolume)/2
            totalarabsvolume = totalarabsvolume/volsum                    
            totalegyptionsvolume = float(totalegyptionsvolume)/2
            totalegyptionsvolume = totalegyptionsvolume/volsum
            
            volume.set_value(i, 'totalForeignersVolume', totalforeignersvolume)
            volume.set_value(i, 'totalArabsVolume', totalarabsvolume)
            volume.set_value(i, 'totalEgyptionsVolume', totalegyptionsvolume)
            
            
            ''' Total investors type turnover '''
            totalforeignersturnover = float(totalforeignersturnover)/2
            totalforeignersturnover = totalforeignersturnover/totalturnover                               
            totalarabsturnover= float(totalarabsturnover)/2
            totalarabsturnover = totalarabsturnover/totalturnover                         
            totalegyptionsturnover = float(totalegyptionsturnover)/2
            totalegyptionsturnover = totalegyptionsturnover/totalturnover
            
            volume.set_value(i, 'totalForeignersTurnOver', totalforeignersturnover)
            volume.set_value(i, 'totalArabsTurnOver', totalarabsturnover)
            volume.set_value(i, 'totalEgyptionsTurnOver', totalegyptionsturnover)
            
            
            ''' BUYER OR SELLER '''
            
            retailbuyerorseller = retailbuyer - retailseller
            volume.set_value(i, 'retailBuyerOrSeller', retailbuyerorseller)
            retailbuyerorseller

            institutesbuyerorseller = institutesbuyer - institutesseller
            volume.set_value(i, 'institutesBuyerOrSeller', institutesbuyerorseller)

            foreignerbuyerorseller = foreignerbuyer - foreignerseller
            volume.set_value(i, 'foreignerBuyerOrSeller', foreignerbuyerorseller)
            
            arabbuyerorseller = arabbuyer -arabseller
            volume.set_value(i, 'arabBuyerOrSeller', arabbuyerorseller)
            
            egyptionbuyerorseller = egyptionbuyer - egyptionseller
            volume.set_value(i, 'egyptionBuyerOrSeller', egyptionbuyerorseller)
            
            

            volsum = row['Volume']
            totalturnover = row['TurnOver']
            institutesbuyerorseller = 0.0
            
            
            if (volume.get_value(index, 'Type', takeable=False)) == "Retail":    
                totalretailvolume = row['Volume'] 
                totalretailturnover = row ['TurnOver']
                totalinistitutesvolume = 0
                totalinistitutesturnover = 0
                
                institutesbuyer = 0
                institutesseller = 0
                
                if (row['Trans'] == 'Buy'):
                    retailbuyer = row['Volume']
                    retailseller = 0
                    
                #never entered    
                else:
                    retailseller = row['Volume']
                    retailbuyer = 0
              
            #never entered    
            else:
                totalretailvolume = 0
                totalretailturnover = 0
                totalinistitutesvolume = row['Volume'] 
                totalretailturnover = row['TurnOver'] 
                
                if (row['Trans'] == 'Buy'):
                    
                    institutesbuyer = row['Volume']
                    institutesseller = 0
                else:
                    institutesseller = row['Volume']
                    institutesbuyer = 0

            
            if (volume.get_value(index, 'Investor', takeable=False)) == "Foreigners":    
                totalforeignersvolume = row['Volume'] 
                totalforeignersturnover = row ['TurnOver']
                totalarabsvolume = 0
                totalegyptionsvolume = 0
                totalarabsturnover = 0
                totalegyptionsturnover = 0
                
                arabbuyer = 0
                arabseller = 0
                
                egyptionbuyer = 0
                egyptionseller = 0
                
                if (row['Trans'] == 'Buy'):
                    foreignerbuyer = row['Volume']
                    foreignerseller = 0
                    
                else:
                    foreignerseller = row['Volume']
                    foreignerbuyer = 0
                
                
            elif(volume.get_value(index, 'Investor', takeable=False)) == "Arabs":
                totalarabsvolume = row['Volume'] 
                totalarabsturnover = row ['TurnOver']
                totalforeignersvolume = 0
                totalforeignersturnover = 0
                totalegyptionsvolume = 0
                totalegyptionsturnover = 0
                
                
                foreignerbuyer = 0
                foreignerseller = 0
                
                egyptionbuyer = 0
                egyptionseller = 0
                
                if (row['Trans'] == 'Buy'):
                    arabbuyer = row['Volume']
                    arabseller = 0
                else:
                    arabseller = row['Volume']
                    arabbuyer = 0
                
                
                
            else:
                totalegyptionsvolume = row['Volume'] 
                totalegyptionsturnover = row ['TurnOver']
                totalforeignersvolume = 0
                totalforeignersturnover = 0
                totalarabsvolume = 0
                totalarabsturnover = 0
                
                foreignerbuyer = 0
                foreignerseller = 0
                
                arabbuyer = 0
                arabseller = 0
                
                if (row['Trans'] == 'Buy'):
                    egyptionbuyer = row['Volume']
                    egyptionseller = 0
                else:
                    egyptionseller = row['Volume']
                    egyptionbuyer = 0
                    
                


            i = index 
                
        oldDate = row['Date']
        
        
        
    
    volume = volume.query('volumeSum != 0')
    volume = volume.reset_index()
    volume = volume.drop('index', 1)
    
   
    indexVsVol = pd.merge(indexVsVol, volume, left_on = 'Date (GMT)' ,right_on = 'Date')
    
    
    return indexVsVol
















''' ----------------MAIN-------------------- '''

indexFile = readData('Copy of EGX.xlsx')
indexData=indexFile['Copy of EGX']

indexData['Date (GMT)'] = pd.to_datetime(indexData['Date (GMT)'], format="%Y/%m/%d")
     






indexCompositionData = pd.read_csv('Trading Composition Data.csv', dayfirst=True, parse_dates=True,delimiter=";")

indexCompositionData['Date']=pd.to_datetime(indexCompositionData['Date'],errors='coerce')




indexVsVol = indexVsVol(indexData,indexCompositionData)
        
