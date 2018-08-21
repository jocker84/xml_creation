# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 19:26:43 2018

@author: Jocker
"""

import sys
import os

class xml:
    
    def init(self,
            path     = "C:/Users/Jocker/Deskto",
            file     = "test.xml", 
            ):
        
        self.path = path
        self.file = file
        
        f1 = open(path+'/'+file,'w+')  
        f1.write("")
        f1.close()
        
        
    def Subdie(self,
            subdie     = "DUT1",
            x        = 0,
            y        = 0
    
            ):
    
        self.subdie = subdie
        
        file_temp = """
            <Subdie>
                <Subname>{subdie}</Subname>
                <Coordinates>
                    <x-Value>{x}</x-Value>
                    <y-Value>{x}</y-Value>
                </Coordinates>
            </Subdie>
        """
        
        context_top = {
    
            "subdie": subdie,
            "x": x,
            "y": y
            }
    
        f1 = open(path+'/'+file,'a+')  
        f1.write(file_temp.format(**context_top))
        f1.close()


    def Switch(self,
            SMU1  = [],
            SMU2  = [],
            SMU3  = [],
            SMU4  = [],
            SMU5  = [],
            SMU6  = [],
            SMU7  = [],
            SMU8  = [],
            SMU9  = [],
            SMU10 = [],
            SMU11 = [],
            SMU12 = [],
            SMU13 = [],
            SMU14 = [],
            SMU15 = [],
            SMU16 = [],
            ):
    
    
        file_temp = """

            <connect>
            
                {switch}
            </connect>

        """
        
        switch = "\n"
        if len(SMU1) >0: switch += "\t<SMU1>" +','.join('{:d}'.format(e) for e in sorted(SMU1))+"," + "</SMU1>\n"
        if len(SMU2) >0: switch += "\t<SMU2>" +','.join('{:d}'.format(e) for e in sorted(SMU2))+"," + "</SMU2>\n"
        if len(SMU3) >0: switch += "\t<SMU3>" +','.join('{:d}'.format(e) for e in sorted(SMU3))+"," + "</SMU3>\n"    
        if len(SMU4) >0: switch += "\t<SMU4>" +','.join('{:d}'.format(e) for e in sorted(SMU4))+"," + "</SMU4>\n"
        if len(SMU5) >0: switch += "\t<SMU5>" +','.join('{:d}'.format(e) for e in sorted(SMU5))+"," + "</SMU5>\n"
        if len(SMU6) >0: switch += "\t<SMU6>" +','.join('{:d}'.format(e) for e in sorted(SMU6))+"," + "</SMU6>\n"
        if len(SMU7) >0: switch += "\t<SMU7>" +','.join('{:d}'.format(e) for e in sorted(SMU7))+"," + "</SMU7>\n"
        if len(SMU8) >0: switch += "\t<SMU8>" +','.join('{:d}'.format(e) for e in sorted(SMU8))+"," + "</SMU8>\n"
        if len(SMU9) >0: switch += "\t<SMU9>" +','.join('{:d}'.format(e) for e in sorted(SMU9))+"," + "</SMU9>\n"
        if len(SMU10)>0: switch += "\t<SMU10>"+','.join('{:d}'.format(e) for e in sorted(SMU10))+"," + "</SMU10>\n"
        if len(SMU11)>0: switch += "\t<SMU11>"+','.join('{:d}'.format(e) for e in sorted(SMU11))+"," + "</SMU11>\n"
        if len(SMU12)>0: switch += "\t<SMU12>"+','.join('{:d}'.format(e) for e in sorted(SMU12))+"," + "</SMU12>\n"
        if len(SMU13)>0: switch += "\t<SMU13>"+','.join('{:d}'.format(e) for e in sorted(SMU13))+"," + "</SMU13>\n"        
        if len(SMU14)>0: switch += "\t<SMU14>"+','.join('{:d}'.format(e) for e in sorted(SMU14))+"," + "</SMU14>\n"        
        if len(SMU15)>0: switch += "\t<SMU15>"+','.join('{:d}'.format(e) for e in sorted(SMU15))+"," + "</SMU15>\n"        
        if len(SMU16)>0: switch += "\t<SMU16>"+','.join('{:d}'.format(e) for e in sorted(SMU16))+"," + "</SMU16>\n"
    
        context_top = {"switch": switch}
    
        f1 = open(self.path+'/'+self.file,'a+')  
        f1.write(file_temp.format(**context_top))
        f1.close()
    
    def SeqArb3PU(self,

                plot_waveform   = 'False',
                
                meas_name       = 'Dummy Measurements',     
                
                SegmentVolt1    = [],
                SegmentVolt2    = [],
                SegmentVolt3    = [],
                SegmentVolt4    = [],                
                SegmentVolt5    = [],
                SegmentVolt6    = [],  
                
                SegmentTime     = [],
                SegmentMeas     = [],
                SegmentID       = [],
                SegmentTrigger  = [],
                Sequences       = [],
                SequenceCycles  = [],
                SupplyVoltage   = [+0.0,+0.0,+0.0,+0.0,+0.0,+0.0,+0.0,+0.0],
                
                CurrentRange1   = 1E-3,
                CurrentRange2   = 1E-3,
                CurrentRange3   = 1E-3,
                CurrentRange4   = 1E-3,

                VoltageRange1   = 10,
                VoltageRange2   = 10,
                VoltageRange3   = 10,
                VoltageRange4   = 10,
                VoltageRange5   = 10,
                VoltageRange6   = 10,
                
                PulseLoad       = 1e6
                ):


        SegmentVoltSize = max([len(SegmentVolt1), len(SegmentVolt2), len(SegmentVolt3), len(SegmentVolt4), len(SegmentVolt5), len(SegmentVolt6)])

        if len(SegmentVolt1)    == 0: SegmentVolt1   = [0]*SegmentVoltSize
        if len(SegmentVolt2)    == 0: SegmentVolt2   = [0]*SegmentVoltSize        
        if len(SegmentVolt3)    == 0: SegmentVolt3   = [0]*SegmentVoltSize
        if len(SegmentVolt4)    == 0: SegmentVolt4   = [0]*SegmentVoltSize 
        if len(SegmentVolt5)    == 0: SegmentVolt5   = [0]*SegmentVoltSize
        if len(SegmentVolt6)    == 0: SegmentVolt6   = [0]*SegmentVoltSize 
        
        if len(SegmentMeas)     == 0: SegmentMeas    = [0]*(SegmentVoltSize-1)
        if len(SegmentID)       == 0: SegmentID      = [1]*(SegmentVoltSize-1)
        if len(SegmentTrigger)  == 0: SegmentTrigger = [0]*(SegmentVoltSize-1)
        if len(Sequences)       == 0: Sequences      = [1]
        if len(SequenceCycles)  == 0: SequenceCycles = [1]     

        self.ErrorCheck = 0
        if ( SegmentVoltSize < 4 ):
            print( "ERROR: SegmentVolt arrays must be at least 4 values. Change size of SegmentVolt arrays to be at least {:d}.".format(4) )
            self.ErrorCheck = 1

        if ( len(SegmentVolt1) > SegmentVoltSize or len(SegmentVolt1) < SegmentVoltSize ):
            print( "ERROR: SegmentVolt1 array not the same size as SegmentVolt arrays. Change size of SegmentVolt1 array to be at least {:d}.".format(SegmentVoltSize) )
            self.ErrorCheck = 1

        if ( len(SegmentVolt2) > SegmentVoltSize or len(SegmentVolt2) < SegmentVoltSize ):
            print( "ERROR: SegmentVolt2 array not the same size as SegmentVolt arrays. Change size of SegmentVolt2 array to be at least {:d}.".format(SegmentVoltSize) )
            self.ErrorCheck = 1 

        if ( len(SegmentVolt3) > SegmentVoltSize or len(SegmentVolt3) < SegmentVoltSize ):
            print( "ERROR: SegmentVolt3 array not the same size as SegmentVolt arrays. Change size of SegmentVolt3 array to be at least {:d}.".format(SegmentVoltSize) )
            self.ErrorCheck = 1

        if ( len(SegmentVolt4) > SegmentVoltSize or len(SegmentVolt4) < SegmentVoltSize ):
            print( "ERROR: SegmentVolt4 array not the same size as SegmentVolt arrays. Change size of SegmentVolt4 array to be at least {:d}.".format(SegmentVoltSize) )
            self.ErrorCheck = 1           

        if ( len(SegmentVolt5) > SegmentVoltSize or len(SegmentVolt5) < SegmentVoltSize ):
            print( "ERROR: SegmentVolt5 array not the same size as SegmentVolt arrays. Change size of SegmentVolt5 array to be at least {:d}.".format(SegmentVoltSize) )
            self.ErrorCheck = 1       

        if ( len(SegmentVolt6) > SegmentVoltSize or len(SegmentVolt6) < SegmentVoltSize ):
            print( "ERROR: SegmentVolt6 array not the same size as SegmentVolt arrays. Change size of SegmentVolt6 array to be at least {:d}.".format(SegmentVoltSize) )
            self.ErrorCheck = 1       
            
        if ( SegmentVoltSize > len(SegmentTime)+1 or SegmentVoltSize < len(SegmentTime)+1 ):
            print( "ERROR: SegmentVolt1 array not the same size -1 as SegmentTime array. Change size of SegmentTime array to be at least {:d}.".format(len(SegmentVolt1)-1) )
            self.ErrorCheck = 1
            
        if ( SegmentVoltSize > len(SegmentID)+1 or SegmentVoltSize < len(SegmentID)+1 ):
            print( "ERROR: SegmentVolt1 array not the same size -1 as SegmentID array. Change size of SegmentID array to be at least {:d}.".format(len(SegmentVolt1)-1) )
            self.ErrorCheck = 1
            
        if ( SegmentVoltSize > len(SegmentMeas)+1 or SegmentVoltSize < len(SegmentMeas)+1 ):
            print( "ERROR: SegmentVolt1 array not the same size -1 as SegmentMeas array. Change size of SegmentMeas array to be at least {:d}.".format(len(SegmentVolt1)-1) )
            self.ErrorCheck = 1
            
        if ( SegmentVoltSize > len(SegmentTrigger)+1 or SegmentVoltSize < len(SegmentTrigger)+1 ):
            print( "ERROR: SegmentVolt1 array not the same size -1 as SegmentTrigger array. Change size of SegmentTrigger array to be at least {:d}.".format(len(SegmentVolt1)-1) )
            self.ErrorCheck = 1
            
        if ( len(Sequences) > len(SequenceCycles) or len(Sequences) < len(SequenceCycles) ):
            print( "ERROR: Sequence array not the same size as SequenceCycle array. Change size of SequenceCycle array size to be at least {:d}.".format(len(Sequences)) )
            self.ErrorCheck = 1
    
        for SegNum in range(len(SegmentTime)):
           if ( SegmentTime[SegNum] < 20e-9  ):            
                print( "ERROR: time is smaller as the minimum value of 20 ns for SegmentTime element {:d}.".format(SegNum+1) )
                self.ErrorCheck = 1
           if ( SegmentTime[SegNum] > 20 ):
                print( "ERROR: time is longer as the maximum value of 20 s for SegmentTime element {:d}. Please cycle the Sequence to acchieve longer times".format(SegNum+1))
                self.ErrorCheck = 1

    
        for SegNum in range(len(SegmentTime)):
            slew1 =  abs(SegmentVolt1[SegNum] - SegmentVolt1[SegNum+1])/SegmentTime[SegNum]
            slew2 =  abs(SegmentVolt2[SegNum] - SegmentVolt2[SegNum+1])/SegmentTime[SegNum]
            slew3 =  abs(SegmentVolt3[SegNum] - SegmentVolt3[SegNum+1])/SegmentTime[SegNum]
            slew4 =  abs(SegmentVolt4[SegNum] - SegmentVolt4[SegNum+1])/SegmentTime[SegNum]
            slew5 =  abs(SegmentVolt5[SegNum] - SegmentVolt5[SegNum+1])/SegmentTime[SegNum]
            slew6 =  abs(SegmentVolt6[SegNum] - SegmentVolt6[SegNum+1])/SegmentTime[SegNum]
            
            if ( slew1 == 0 ): slew1 = 10000
            if ( slew2 == 0 ): slew2 = 10000
            if ( slew3 == 0 ): slew3 = 10000
            if ( slew4 == 0 ): slew4 = 10000 
            if ( slew5 == 0 ): slew5 = 10000
            if ( slew6 == 0 ): slew6 = 10000
           
            if ( slew1 < 1000 ): 
                print( "ERROR: slew rate of channel 1 is slower as the maximum value of 1 V/ms for SegmentTime element {:d}.".format(SegNum+1))
                self.ErrorCheck = 1
            if ( slew2 < 1000 ): 
                print( "ERROR: slew rate of channel 2 is slower as the maximum value of 1 V/ms for SegmentTime element {:d}.".format(SegNum+1))
                self.ErrorCheck = 1
            if ( slew3 < 1000 ): 
                print( "ERROR: slew rate of channel 3 is slower as the maximum value of 1 V/ms for SegmentTime element {:d}.".format(SegNum+1))
                self.ErrorCheck = 1
            if ( slew4 < 1000 ): 
                print( "ERROR: slew rate of channel 4 is slower as the maximum value of 1 V/ms for SegmentTime element {:d}.".format(SegNum+1))
                self.ErrorCheck = 1
            if ( slew5 < 1000 ): 
                print( "ERROR: slew rate of channel 5 is slower as the maximum value of 1 V/ms for SegmentTime element {:d}.".format(SegNum+1))
                self.ErrorCheck = 1                
            if ( slew6 < 1000 ): 
                print( "ERROR: slew rate of channel 6 is slower as the maximum value of 1 V/ms for SegmentTime element {:d}.".format(SegNum+1))
                self.ErrorCheck = 1           
        
        
        NumMeasSpots  = 0
        if (self.ErrorCheck == 0):  
            SeqNumMeasSpots  = [0]*512
            SeqTotalMeasTime = [0]*512
            SegTotalCount = 0
            
            for SeqID in range(512):
                
                SegCount     = 0
                SeqMeasSpots = 0
                SeqMeasTime  = 0
                
                for SegNum in range(len(SegmentVolt2)-1):          
                     if (SegmentID[SegNum] == SeqID and SegmentMeas[SegNum] < 1):
                         SegCount = SegCount + 1
        
                     if (SegmentID[SegNum] == SeqID and SegmentMeas[SegNum] > 0):
                          divmax = SegmentMeas[SegNum]
                          if ( SegmentTime[SegNum] / SegmentMeas[SegNum] < 20e-9 ):
                             divmax = int(SegmentTime[SegNum] / 20e-9)
                             #print( "WARNING: Measurement Segment time too short for minimum segment time of 20 ns. Amount of measurement segments was changed to {:d} with 20 ns segment time.".format(divmax))
                          
                          for DivSeg in range(divmax): 
                             SegCount = SegCount + 1
                            
                             if (SegmentMeas[SegNum]>0):
                                  SeqMeasSpots = SeqMeasSpots + 1
                                  SeqMeasTime  = SeqMeasTime + SegmentTime[SegNum] / divmax
               
                SeqNumMeasSpots[SeqID]  = SeqMeasSpots
                SeqTotalMeasTime[SeqID] = SeqMeasTime
        
                SegTotalCount           = SegTotalCount + SegCount
        
     
            if (SegTotalCount > 2048):
                print("ERROR: Total number of segments exceeds maximum number of 2048 (every measurement points counts as Segment). Number of total segments is {:d}.".format(SegTotalCount))
                self.ErrorCheck = 1
            #else:
                #print("WARNING: Number of total segments is {:d} out of 2048.".format(SegTotalCount))
                
        if (self.ErrorCheck == 0):         
            
            TotalMeasTime = 0
            NumMeasSpots  = 0
            for Seq in range(len(Sequences)): 
                TotalMeasTime = TotalMeasTime + SeqTotalMeasTime[Sequences[Seq]] * SequenceCycles[Seq]
                NumMeasSpots  = NumMeasSpots  + SeqNumMeasSpots[Sequences[Seq]]  * SequenceCycles[Seq]
        
            SampleRate = 200E+6
            
            NumTotalSamples = int(TotalMeasTime*SampleRate)
            RateFactor      = int((NumTotalSamples/1e6)+1)
            SampleRate      = (SampleRate/RateFactor)
            NumTotalSamples = int(TotalMeasTime*SampleRate)
        
        
            #if ( SampleRate < 200E+6 ):
                #print("WARNING: Maximum sample rate of 2e+008 points/sec is reduced by a factor of %d to %g points/sec.", RateFactor, SampleRate )
         
            if ( NumMeasSpots > 8000 ):
                print( "ERROR: Total Number of Measurements Points {:d}. Reduce the number of measurement points to be at maximum 8000.".format(NumMeasSpots))
                self.ErrorCheck = 1
            #else:
                #print("WARNING: Number of total output values is %d out of %d.", NumMeasSpots, 8000)

        if (self.ErrorCheck == 0):    
   
            self.TimeStep = [0]
            self.Voltage1  = []
            self.Voltage2  = []
            self.Voltage3  = []
            self.Voltage4  = []
            self.Voltage5  = []
            self.Voltage6  = []
            self.ID        = [SegmentID[0]]
            self.Cycle     = [1]
            self.Meas      = [SegmentMeas[0]]
            
            for Seq in range(len(Sequences)):
                for cyc in range(SequenceCycles[Seq]):
                    for SegNum in range(len(SegmentID)):
                        if Sequences[Seq] == SegmentID[SegNum]:
            
                                if (SegmentMeas[SegNum] > 0):
                                    self.Voltage1 += linspace(SegmentVolt1[SegNum],SegmentVolt1[SegNum+1],SegmentMeas[SegNum]).tolist()
                                    self.Voltage2 += linspace(SegmentVolt2[SegNum],SegmentVolt2[SegNum+1],SegmentMeas[SegNum]).tolist()
                                    self.Voltage3 += linspace(SegmentVolt3[SegNum],SegmentVolt3[SegNum+1],SegmentMeas[SegNum]).tolist()
                                    self.Voltage4 += linspace(SegmentVolt4[SegNum],SegmentVolt4[SegNum+1],SegmentMeas[SegNum]).tolist()
                                    self.Voltage5 += linspace(SegmentVolt5[SegNum],SegmentVolt5[SegNum+1],SegmentMeas[SegNum]).tolist()
                                    self.Voltage6 += linspace(SegmentVolt6[SegNum],SegmentVolt6[SegNum+1],SegmentMeas[SegNum]).tolist()
                                    
                                    self.TimeStep += [SegmentTime[SegNum]/SegmentMeas[SegNum]]*SegmentMeas[SegNum]
                                    self.ID       += [SegmentID[SegNum]]*SegmentMeas[SegNum]
                                    self.Cycle    += [cyc+1]*SegmentMeas[SegNum]
                                    self.Meas     += [1]*SegmentMeas[SegNum]
                                    
                                if (SegmentMeas[SegNum] == 0):
                                    self.Voltage1 += [SegmentVolt1[SegNum]]
                                    self.Voltage2 += [SegmentVolt2[SegNum]]                        
                                    self.Voltage3 += [SegmentVolt3[SegNum]]                        
                                    self.Voltage4 += [SegmentVolt4[SegNum]]
                                    self.Voltage5 += [SegmentVolt5[SegNum]]     
                                    self.Voltage6 += [SegmentVolt6[SegNum]]
                                    
                                    self.TimeStep += [SegmentTime[SegNum]] 
                                    self.ID       += [SegmentID[SegNum]] 
                                    self.Cycle    += [cyc+1]
                                    self.Meas     += [0]

            self.Voltage1 += [SegmentVolt1[SegNum+1]]
            self.Voltage2 += [SegmentVolt2[SegNum+1]]                        
            self.Voltage3 += [SegmentVolt3[SegNum+1]]                        
            self.Voltage4 += [SegmentVolt4[SegNum+1]]
            self.Voltage5 += [SegmentVolt5[SegNum+1]]     
            self.Voltage6 += [SegmentVolt6[SegNum+1]]
             
            if plot_waveform == True:              
                figure(meas_name)                    
                self.Time = cumsum(self.TimeStep)/1E-6
                plot(self.Time, self.Voltage1, '.-', label = "Voltage1")
                plot(self.Time, self.Voltage2,'.-', label = "Voltage2")
                plot(self.Time, self.Voltage3,'.-', label = "Voltage3")
                plot(self.Time, self.Voltage4,'.-', label = "Voltage4")
                plot(self.Time, self.Voltage5,'.-', label = "Voltage5")
                plot(self.Time, self.Voltage6,'.-', label = "Voltage6")
                legend(loc="upper left")
                minorticks_on()
                xlabel('Time [us]')
                ylabel('Voltage [V]')
    
                twinx()
                step(self.Time, self.ID, label = "ID", linestyle = "solid", color = "darkgreen") 
                step(self.Time, self.Cycle, label = "Cycle #", linestyle = "dashed", color ="black")
                step(self.Time, self.Meas, label = "Meas", linestyle = "dashed", color = "blue") 
                legend(loc="upper right")
                ylabel('#') 
            
            
            file_temp = """
    
            <CallUTM>
                <Name>{meas_name}</Name>
                <UserLib>Transients</UserLib>
                <UserModul>SeqArb3PU_v1</UserModul>
                
                <SegmentVolt1>{SegmentVolt1}</SegmentVolt1><Size>{SegmentVolt1_Size}</Size>
                <SegmentVolt2>{SegmentVolt2}</SegmentVolt2><Size>{SegmentVolt2_Size}</Size>
                <SegmentVolt3>{SegmentVolt3}</SegmentVolt3><Size>{SegmentVolt3_Size}</Size>
                <SegmentVolt4>{SegmentVolt4}</SegmentVolt4><Size>{SegmentVolt4_Size}</Size>            
                <SegmentVolt5>{SegmentVolt5}</SegmentVolt5><Size>{SegmentVolt5_Size}</Size>
                <SegmentVolt6>{SegmentVolt6}</SegmentVolt6><Size>{SegmentVolt6_Size}</Size>            
                
                <SegmentTime>{SegmentTime}</SegmentTime><Size>{SegmentTime_Size}</Size>
                <SegmentID>{SegmentID}</SegmentID><Size>{SegmentID_Size}</Size>
                <SegmentMeas>{SegmentMeas}</SegmentMeas><Size>{SegmentMeas_Size}</Size>
                <SegmentTrigger>{SegmentTrigger}</SegmentTrigger><Size>{SegmentTrigger_Size}</Size>
        
                <Sequences>{Sequences}</Sequences><Size>{Sequences_Size}</Size>
                <SequenceCycles>{SequenceCycles}</SequenceCycles><Size>{SequenceCycles_Size}</Size>
        
                <CurrentRange1>{CurrentRange1}</CurrentRange1> 
                <CurrentRange2>{CurrentRange2}</CurrentRange2>             
                <CurrentRange3>{CurrentRange3}</CurrentRange3>             
                <CurrentRange4>{CurrentRange4}</CurrentRange4>             
                
                <VoltageRange1>{VoltageRange1}</VoltageRange1> 
                <VoltageRange2>{VoltageRange2}</VoltageRange2>             
                <VoltageRange3>{VoltageRange3}</VoltageRange3>            
                <VoltageRange4>{VoltageRange4}</VoltageRange4>            
                <VoltageRange5>{VoltageRange5}</VoltageRange5> 
                <VoltageRange6>{VoltageRange6}</VoltageRange6>             
    
                <PulseLoad>{PulseLoad}</PulseLoad>
        
                <SupplyVoltage>{SupplyVoltage}</SupplyVoltage><Size>8</Size>
        
                <ReadParameters>
                    <Time>{Time}</Time>
                    <Current1>{Current1}</Current1>
                    <Current2>{Current2}</Current2>
                    <Current3>{Current3}</Current3>
                    <Current4>{Current4}</Current4>            
                    <Voltage1>{Voltage1}</Voltage1>
                    <Voltage2>{Voltage2}</Voltage2>
                    <Voltage3>{Voltage3}</Voltage3>
                    <Voltage4>{Voltage4}</Voltage4>                
                </ReadParameters>
            </CallUTM>\n
           
            <Save>{meas_name}_T.dat<< ''&format(§{meas_name}§Time§;%.2e)</Save>
            <Save>{meas_name}_V1.dat<< ''&format(§{meas_name}§Voltage1§;%.2f)</Save>
            <Save>{meas_name}_V2.dat<< ''&format(§{meas_name}§Voltage2§;%.2f)</Save>
            <Save>{meas_name}_V3.dat<< ''&format(§{meas_name}§Voltage3§;%.2f)</Save>
            <Save>{meas_name}_V4.dat<< ''&format(§{meas_name}§Voltage4§;%.2f)</Save>
            <Save>{meas_name}_I1.dat<< ''&format(§{meas_name}§Current1§;%.2e)</Save>
            <Save>{meas_name}_I2.dat<< ''&format(§{meas_name}§Current2§;%.2e)</Save>
            <Save>{meas_name}_I3.dat<< ''&format(§{meas_name}§Current3§;%.2e)</Save>
            <Save>{meas_name}_I4.dat<< ''&format(§{meas_name}§Current4§;%.2e)</Save>
    
            """
        
            context_top = {
        
                "meas_name":            meas_name,
            
                "SegmentVolt1":         ';'.join('{:+.2f}'.format(e) for e in SegmentVolt1),
                "SegmentVolt2":         ';'.join('{:+.2f}'.format(e) for e in SegmentVolt2),
                "SegmentVolt3":         ';'.join('{:+.2f}'.format(e) for e in SegmentVolt3),
                "SegmentVolt4":         ';'.join('{:+.2f}'.format(e) for e in SegmentVolt4),           
                "SegmentVolt5":         ';'.join('{:+.2f}'.format(e) for e in SegmentVolt5),
                "SegmentVolt6":         ';'.join('{:+.2f}'.format(e) for e in SegmentVolt6),
     
                "SegmentVolt1_Size":    str(len(SegmentVolt1)),
                "SegmentVolt2_Size":    str(len(SegmentVolt2)),
                "SegmentVolt3_Size":    str(len(SegmentVolt3)),
                "SegmentVolt4_Size":    str(len(SegmentVolt4)),
                "SegmentVolt5_Size":    str(len(SegmentVolt5)),
                "SegmentVolt6_Size":    str(len(SegmentVolt6)),   
    
               
                "SegmentTime":          ';'.join('{:.2E}'.format(e) for e in SegmentTime),
                "SegmentID":            ';'.join('{:d}'.format(e)  for e in SegmentID),
                "SegmentMeas":          ';'.join('{:d}'.format(e) for e in SegmentMeas),
                "SegmentTrigger":       ';'.join('{:d}'.format(e) for e in SegmentTrigger),
                "Sequences":            ';'.join('{:d}'.format(e) for e in Sequences),
                "SequenceCycles":       ';'.join('{:d}'.format(e) for e in SequenceCycles),
    
                "SegmentTime_Size":     str(len(SegmentTrigger)),
                "SegmentID_Size":       str(len(SegmentTime)),
                "SegmentMeas_Size":     str(len(SegmentMeas)),
                "SegmentTrigger_Size":  str(len(SegmentID)),
                "Sequences_Size":       str(len(Sequences)),
                "SequenceCycles_Size":  str(len(SequenceCycles)),
                "SupplyVoltage_Size":   str(len(SupplyVoltage)),
               
                "CurrentRange1":        '{:.0E}'.format(CurrentRange1),
                "CurrentRange2":        '{:.0E}'.format(CurrentRange2),
                "CurrentRange3":        '{:.0E}'.format(CurrentRange3),
                "CurrentRange4":        '{:.0E}'.format(CurrentRange4),
    
                "VoltageRange1":        '{:d}'.format(VoltageRange1),
                "VoltageRange2":        '{:d}'.format(VoltageRange2),
                "VoltageRange3":        '{:d}'.format(VoltageRange3),
                "VoltageRange4":        '{:d}'.format(VoltageRange4),
                "VoltageRange5":        '{:d}'.format(VoltageRange5),
                "VoltageRange6":        '{:d}'.format(VoltageRange6),
                
                "PulseLoad":            '{:.0E}'.format(PulseLoad),
                
                "SupplyVoltage":        ';'.join('{:+.2f}'.format(e) for e in SupplyVoltage),
    
                "Time":                 str(NumMeasSpots),
                "Current1":             str(NumMeasSpots),
                "Current2":             str(NumMeasSpots),
                "Current3":             str(NumMeasSpots),
                "Current4":             str(NumMeasSpots),
                "Voltage1":             str(NumMeasSpots),
                "Voltage2":             str(NumMeasSpots),
                "Voltage3":             str(NumMeasSpots),
                "Voltage4":             str(NumMeasSpots)        
                }
    
    
            
            f1 = open(self.path+'/'+self.file,'a+')  
            f1.write(file_temp.format(**context_top))
            f1.close()



xml = xml()



