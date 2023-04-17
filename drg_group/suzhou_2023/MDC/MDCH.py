from drg_group.suzhou_2023.Base import message,intersect,SS_VALID
from drg_group.suzhou_2023.ADRG import HB1,HC1,HC2,HC3,HJ1,HK1,HL1,HL2,HR1,HS1,HS2,HS3,HT1,HT2,HU1,HZ1,HZ2,HZ3

def group(record):
  mdc_zd=["C23.x00","K80.000x002","K81.007","S36.110","B15.900","T86.400x003","K74.301+I98.2*","T82.813","K83.017","Q45.100","S36.100x081","K81.000x008","K91.800x403","Q85.900x019","D37.603","T85.800x802","T81.800x006","K71.900x003","K76.700x003","Q85.900x044","M32.108+K77.8*","K74.611","B54.x00x003+K77.0*","K74.619+I98.2*","B17.100","K83.800x009","Q44.504","K82.400","B17.200","K73.800x001","K70.302+I98.3*","K71.100x005","S36.100x011","K92.800x009","K83.818","K83.803","K75.300x001","K74.300x005+I98.2*","E80.603","B16.901","K83.307","K76.809","C25.000","B17.102","K83.007","K70.301+I98.2*","K86.814","K76.815","K91.800x301","D17.700x015","K76.101","B16.100","Q44.001","K76.808","Q44.700x002","K72.002","K76.800x007","B16.204","B18.204","K71.701","K76.102","B17.200x004","K76.810","K70.300","K80.505","K83.013","K85.000","K86.100x001","Q27.304","Q45.802","D01.501","B16.200","I72.809","C25.800x001","D13.500x001","B18.805","B19.002","B65.900x010+K77.0*","E80.600x005","K86.200","C22.101","K74.620+I98.2*","K76.500x001","D01.701","B25.100+K77.0*","K80.400x004","K80.403","K74.600x034","K85.302","K81.008","S36.100x013","Q45.200","K83.817","K82.806","B26.802+K77.0*","Q85.911","A51.400x008+K77.0*","K75.800x001","Q44.505","K80.507","C25.300","K71.100x003","B66.301","K83.304","K81.100","K74.600","K85.801","I74.804","K70.201","K86.808","S36.200x001","K75.002","K75.200","D18.000x031","K74.600x027","K70.400x002","K75.400","K86.105","A52.700x007+K77.0*","K91.800x304","C25.802","M35.003+K77.8*","S36.200x031","K82.801","K86.100x004","B16.100x003","K76.800x027","K86.800x001","Q44.701","B15.901","K86.817","K80.404","K86.803","S36.100x031","R16.000x001","K71.000x002","C45.704","K70.001","S36.100x021","K83.106","K83.000x012","B16.902","R93.302","K74.302+I98.3*","K83.105","K76.800x023","D37.600x002","K91.500","K76.500x002","B17.803","K74.600x029","K75.901","K74.610","K86.818","K85.816","K72.005","Q44.500x007","K71.500x002","T86.400x016","K80.304","B18.107","Q27.800x004","K75.810","K71.001","K80.002","D01.700","K71.100x007","K83.019","T86.401","K83.108","C25.803","K74.600x041","K85.813","Q45.001","B18.202","K83.807","K83.305","K80.001","K82.808","R16.200x001","K80.503","K76.700","K86.802","B17.900x006","K82.807","R93.200x001","C24.101","K76.807","K74.608","E80.400","K71.101","K86.300","K76.800x009","D37.705","K76.602","K80.306","K91.800x402","Q45.300x902","B15.905","K70.305+I98.3*","R93.204","B16.101","B17.800x003","K65.007","K76.818","C24.000","K80.406","K83.820","K85.100","Q44.100x002","K82.101","B17.203","K74.606","R93.200x002","B18.903","D13.700x001","K82.000x003","D01.503","C22.900","B44.803","K74.600x030","K83.000x007","K92.800x010","K82.900x002","K76.800x026","K72.100","K80.502","K83.103","K82.200","B18.106","K80.500x001","B66.100x001+K77.0*","B15.001","D37.605","C22.001","K85.802","R93.203","B17.903","I72.800x072","K81.101","K85.821","Q45.301","R17.901","I74.803","I81.x00","B16.903","B18.900","K74.600x021","B17.801","K76.804","K86.801","K76.800x015","K83.819","K74.300x007+I98.2*","N82.201","C24.800","K85.818","K70.306+I98.3*","K71.900","B18.001","K71.104","K83.808","Q44.200","B18.200x009","K76.814","D37.600x003","K75.100","D37.600x001","Q44.500x006","K76.400","K86.816","C22.301","K83.303","I87.109","C24.900","B17.900","K76.816","K83.100x001","S36.113","T86.400x005","K86.100x002","K80.501","K85.902","K73.901","S36.101","B45.800x001","K83.809","Q44.705","K86.800x013","S36.100x051","Q44.101","K86.812","T86.400x006","K83.300","C22.200","K75.401","K75.000x003","K76.803","Q44.703","I87.121","B26.300+K87.1*","T86.800x021","B17.204","B15.000","B58.100+K77.0*","K74.600x025","K76.813","K82.805","K83.008","D13.701","K74.600x036","K83.018","K85.002","K86.107","K91.807","K71.100x006","K85.201","K70.402","K70.403","K76.600x006","K80.300x005","B16.202","K80.200x003","B16.000x001","B17.101","K75.300","K76.200","K83.301","B15.002","B16.905","K81.002","K76.601","Q44.201","K91.840","B18.100","K81.005","D01.500x001","B17.100x006","K85.301","K91.841","S36.103","K82.000","K82.900x001","K74.603","K85.300","Q44.601","B18.003","B17.800x001","D37.604","K76.603","K82.302","I82.000x001","K71.702","C24.004","K71.700","K86.000","K86.101","B15.902","B17.000","K86.807","C24.001","R17.900","K82.800x009","K86.805","Q44.301","K83.101","B18.800x004","K74.616+I98.2*","K80.201","K80.200x001","C78.800x009","D37.600x004","K83.802","K83.100","K83.306","K83.006","K76.401","B18.203","K72.000x013","K91.826","K80.301","S36.112","K82.300","K81.003","K83.816","K91.800x401","K91.800x407","K80.405","K75.806","B17.103","T86.400x012","K85.001","B65.900x004+K77.0*","K80.800x001","K70.303+I98.2*","K80.506","D13.600","I86.809","K72.900x003+G94.3*","T86.400x010","K80.801","K85.817","I86.808","K72.003","C22.100","Q44.702","K71.601","K74.600x010","B17.900x002","C24.800x001","K74.617+I98.3*","C78.806","K80.401","C25.100","K83.800x023","K92.800x012","K73.801","K71.600x002","B16.000","K74.500","K74.300","K71.100","E85.415+K77.8*","Q44.600","K83.005","K74.200","B18.201","K83.100x008","D01.502","C25.401","R93.201","C25.801","B18.000","Q44.400","K85.800x003","K73.200x002","B18.004","B18.800x005","C22.000","K81.001","K85.814","Q44.503","Q44.704","K74.615+I98.3*","B00.802+K77.0*","Q44.700x003","B17.900x005","K82.001","K86.815","K71.500x001","S36.102","D13.500","E80.601","K83.805","K83.102","C25.200","B65.904+I98.2*","K86.800x002","K92.800x006","T86.400x001","T86.400x014","K80.400","K81.900","A18.301","B15.903","B17.205","K86.811","K86.813","A18.814+K77.0*","K85.822","Q85.912","K80.302","K83.302","K80.305","Q44.300","K83.502","B67.800x001+K77.0*","K81.801","K76.600x002","K70.901","K82.305","K91.825","B19.001","K70.000","K82.200x002","I77.000x017","S36.200x021","B05.800x003+K77.0*","B17.100x003","B16.904","E80.501","K76.000","Q44.502","K83.400x001","K74.300x006+I98.3*","K83.814","K80.300x002","B16.100x002","K80.402","K76.901","K83.902","K76.600x007","B54.x00","I87.803","K83.000","B18.800x002","E84.901","K83.011","K76.801","K74.601","B17.800x002","B17.904","B25.200+K87.1*","K74.604","K76.819","B17.900x004","B19.000","K75.000x002","K72.904","D37.706","I82.001","K74.600x042","B15.003","B18.104","B18.804","I74.800x016","K75.001","K83.004","K91.806","K74.600x002","A52.705+K77.0*","K74.618+I98.3*","K74.607","R94.500","C22.700","K76.001","K85.800x001","K72.900x001","K82.800x004","K71.102","K83.001","B18.902","A18.816+K87.0*","K71.002","E80.600x008","K83.401","Q45.002","K71.103","K80.500x002","S36.111","T86.400x007","C24.003","B18.100x007","B16.100x004","C77.203","K74.600x003","K86.809","C24.100","K85.102","S36.200x091","B67.000x001+K77.0*","T86.400x009","K83.010","K82.100x002","K80.101","K85.101","D13.500x003","S36.200x092","B18.900x006","B16.201","K76.300","A18.815+K87.0*","Q44.200x003","B65.202+K77.0*","K71.300x001","B67.500x001+K77.0*","K82.306","K83.200x001","E83.102","C22.400","Q44.002","K74.400","B17.200x005","B17.902","K80.000x004","D13.501","B19.901","K86.806","K80.303","K86.103","K70.900","K85.803","K76.800x022","K91.827","A06.400+K77.0*","Q44.004","T86.400x018","Q44.003","Q45.003","Q45.300x901","K82.802","T86.400x011","K75.805","B16.203","K82.800x002","K86.800x015","K73.000x001","S36.210","K83.016","C25.900","K73.900","K74.613","K74.000","D13.400","K73.100","K82.803","K72.000x005","S36.200","T86.804","K75.804","K75.803","K72.000x004","D18.013","K86.104","K71.901","B17.202","B65.906+I98.3*","K70.304+I98.2*","E80.600x007","N82.302","K85.900","B18.800x003","C25.701","K74.612","K75.000","K80.203","Q45.300x904","B18.800x001","B18.801","K71.600","K76.811","K82.301","D37.602","K74.602","K72.001","K71.400x001","K83.104","K85.807","K74.600x031","K82.303","K85.809","D37.700x003","S36.100x001","K72.004","K85.808","E80.600x006","K82.304","C24.002","K86.106","K76.800x021","K83.901","C25.400","E80.500","C78.700","K83.810","K76.806","C77.204","K76.800x006","T86.400x004","Q44.500x005","K81.006","D37.601","K83.014","K76.900x002","K83.804","K83.109","K83.800x022","B18.105","K80.100x001","K80.202","K83.813","Q44.501","T86.400x017","K74.605","I81.x00x003","K71.903+I98.3*","K83.015","K83.501","Q44.102","B19.900","T86.400x013","K85.901","K76.800x003","B18.901","K81.900x001","K83.107","A18.817+K87.1*","B25.101+K77.0*","B16.001","K85.200","K91.800x411","K85.202","K75.800x006","B18.002","K72.902","K70.401","K71.100x008","Q44.700x004","C78.807","K86.102","K80.504","I77.100x011","K85.900x003","Q27.804","C78.808","Q27.805","Q44.100x003","K70.100","K92.801","D13.401","K76.700x001","K81.004","K74.100","K83.800x012","K83.811","S36.201","S36.202","A50.000x002+K77.0*","C22.300","K75.801","S36.200x011","K74.614","B65.903+K77.0*","A01.001+K77.0*","B00.803+K77.0*","K76.500","K91.822","K91.823","R93.205","B18.200","K85.815","E80.602","Z52.600x001","K76.805","K76.817","T86.400x015","K83.815","K74.300x008+I98.3*","K83.012","R17.900x001","K75.003","S36.100x041","K85.800x002","B18.803","B18.802","K71.200x001","K81.000","K82.804","I87.108","K86.901","K86.804","K71.902+I98.2*","C24.000x007","K83.009","K71.800","K86.810","K85.900x002"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCH入组条件，匹配规则：主诊断匹配')

  result=HB1.group(record)
  if result:
    return result
  result=HC1.group(record)
  if result:
    return result
  result=HC2.group(record)
  if result:
    return result
  result=HC3.group(record)
  if result:
    return result
  result=HJ1.group(record)
  if result:
    return result
  result=HK1.group(record)
  if result:
    return result
  result=HL1.group(record)
  if result:
    return result
  result=HL2.group(record)
  if result:
    return result

  if record.ssList and record.ssList[0] in SS_VALID:
    message('符合HQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'HQY'

  result=HR1.group(record)
  if result:
    return result

  result=HS1.group(record)
  if result:
    return result

  result=HS2.group(record)
  if result:
    return result

  result=HS3.group(record)
  if result:
    return result

  result=HT1.group(record)
  if result:
    return result

  result=HT2.group(record)
  if result:
    return result

  result=HU1.group(record)
  if result:
    return result

  result=HZ1.group(record)
  if result:
    return result

  result=HZ2.group(record)
  if result:
    return result

  result=HZ3.group(record)
  if result:
    return result

  message('不符合MDCH的ADRG入组条件')

