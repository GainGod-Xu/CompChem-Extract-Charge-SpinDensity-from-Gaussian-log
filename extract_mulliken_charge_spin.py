#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os,math,sys
#
filename= sys.argv[1]
ifs = open(filename, 'r')
cs_name =filename[:-4] + '.CS'
ofs = open(cs_name, 'w') 
frames=[]
frame=[]
SCF=[]
maxforce=[]
rmsforce=[]

more_output='false'

while 1:
      line=ifs.readline()
      if not line: break
      data=line.split()
      if len(data)>0: # if true, line is not blank
         if data[0]=='Input' or data[0]=='Standard' or data[0]=='Z-Matrix':
            if data[1]=='orientation:': # Found Standard Orientation
              frame=[]
              line=ifs.readline()  # skip header lines
              line=ifs.readline()  # skip header lines
              line=ifs.readline()  # skip header lines
              line=ifs.readline()  # skip header lines
              line=ifs.readline()  # first line containing atom info
              data=line.split()
              while data[0] != '---------------------------------------------------------------------':
                  
                  atomid=data[0]
                  if   data[1]=='1':   atomtype='H'
                  elif data[1]=='6':   atomtype='C'
                  elif data[1]=='8':   atomtype='O'
                  elif data[1]=='7':   atomtype='N'
                  elif data[1]=='17':  atomtype='Cl'
                  elif data[1]=='9':   atomtype='F' 
                  elif data[1]=='14':  atomtype='Si' 
                  elif data[1]=='16':  atomtype='S'
                  elif data[1]=='5' :  atomtype='B'
                  elif data[1]=='15' : atomtype='P'
                  elif data[1]=='35' : atomtype='Br'
                  elif data[1]=='29' : atomtype='Cu'
                  elif data[1]=='44' : atomtype='Ru'
                  elif data[1]=='53' : atomtype='I'
                  elif data[1]=='3' : atomtype='Li'
                  elif data[1]=='27' : atomtype='Co'
                  elif data[1]=='42' : atomtype='Mo' 
                  elif data[1]=='30' : atomtype='Zn'
                  elif data[1]=='13' : atomtype='Al'
                  elif data[1]=='11' : atomtype='Na'
                  elif data[1]=='19' : atomtype='K'
                  elif data[1]=='74' : atomtype='W'
                  elif data[1]=='47' : atomtype='Ag'
                  elif data[1]=='26' : atomtype='Fe'
                  elif data[1]=='45' : atomtype='Rh'
                  elif data[1]=='46' : atomtype='Pd'
                  elif data[1]=='78' : atomtype='Pt'
                  else: 
                      print (data,'no atom type found, exiting....')
                      exit
                  
                  if len(data)==6: 
                     atomx=data[3]
                     atomy=data[4]
                     atomz=data[5]

                  else: 
                     print ('cannot work out Standard orientation format. exiting..')
                     break 

                  #atominfo=[atomid,atomtype,atomx,atomy,atomz]
                  atominfo=[atomid,atomtype]
                  frame.append(atominfo)
                  line=ifs.readline()
                  data=line.split()

            frames.append(frame)
            #print frames
            #print frame

         if data[0]=='Mulliken' and data[1]=='charges' and data[2] == 'and' and data[3] == 'spin' and data[4] == 'densities:':
            line=ifs.readline() # skip line 0
            for iii in frame:
                line=ifs.readline()
                data=line.split()
                ofs.write( '%2s'% data[0] + '    ' + '%2s' % data[1] + '    ' + '%9.6f' % float(data[2]) + '    ' + '%9.6f' % float(data[3]) + '\n')

         if data[0]=='Mulliken' and data[1]=='charges:':
            line=ifs.readline() # skip line 0
            for iii in frame:
                line=ifs.readline()
                data=line.split()
                ofs.write( '%2s'% data[0] + '    ' + '%2s' % data[1] + '\n')       


         
print ('********************************************')
print ( cs_name + ' is finished on there!')
print ('********************************************')

ifs.close()
ofs.close()

