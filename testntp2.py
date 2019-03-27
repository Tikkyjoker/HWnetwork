import testnewntp
import datetime
import struct
import socket
from time import ctime,gmtime,strftime,time
c = testnewntp.NTPClient()
response = c.request('time.windows.com', version=4)
print('\n\n\n')
print('Leap warning         :',response.leap,testnewntp.leap_to_text(response.leap))
print('Version              :',response.version)
print('Mode                 :',response.mode,testnewntp.mode_to_text(response.mode))
print('Stratum              :',response.stratum,testnewntp.stratum_to_text(response.stratum))
print('Poll time            :',response.poll,)
print('precision second     :',testnewntp.prec_to_sec(response.precision))
print('Root delay           :',response.root_delay)
print('Root Dispersion      :',response.root_dispersion)
print('Reference Identifier :',testnewntp.ref_id_to_text(response.ref_id))
print('Reference Time       :',strftime("%a, %d %b %Y %H:%M:%S", gmtime(response.ref_time)),response.ref_time)
print('Originate Time       :',strftime("%a, %d %b %Y %H:%M:%S", gmtime(response.orig_time)),response.orig_time)
print('Receive Time         :',strftime("%a, %d %b %Y %H:%M:%S", gmtime(response.recv_time)),response.recv_time)
print('Transmit Time        :',strftime("%a, %d %b %Y %H:%M:%S", gmtime(response.tx_time)),response.tx_time)
print('timestamp            :',strftime("%a, %d %b %Y %H:%M:%S", gmtime(response.tx_timestamp)),response.tx_timestamp)
print(strftime("%a, %d %b %Y %H:%M:%S", gmtime(response.tx_time)))
print(response.offset)
print(response.delay)
print('(',response.recv_timestamp,'-',response.orig_timestamp,')+(',response.tx_timestamp,'-',response.dest_timestamp,time(),')/2')


# print('response offset      :',response.offset)
# print('response time        :',response.tx_time)
# print("StrFtime             :",strftime("%a, %d %b %Y %H:%M:%S", gmtime(response.tx_time)))
# print("Ctime original       :",ctime())
# print("Ctime                :",ctime(response.tx_time))
# print("Ctime by time stamp  :",ctime(response.tx_timestamp))
