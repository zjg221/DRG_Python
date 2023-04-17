from drg_group.changzhou_2022.Base import message,intersect,SS_VALID
from drg_group.changzhou_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=["A01.000x016+I41.0*","A18.808+I32.0*","A18.809+I32.0*","A18.821+I41.0*","A36.802+I41.0*","A38.x00x002+I41.0*","A39.500","A39.501+I32.0*","A39.503+I41.0*","A52.000+I98.0*","A52.000x001+I52.0*","A52.005+I52.0*","A52.007+I41.0*","A52.008+I32.0*","A54.804+I41.0*","A54.805+I32.0*","B01.800x001+I41.1*","B05.803","B25.803+I41.1*","B26.803+I41.1*","B33.200","B33.200x001+I32.1*","B33.200x004+I41.1*","B33.201+I41.1*","B49.x15","B57.001+I98.1*","B57.002+I41.2*","B57.200x001","B57.200x003","B57.201+I98.1*","B57.202+I41.2*","B57.202+I41.2*","B58.800x001+I41.2*","B67.903","D18.000x001","D18.000x003","D18.000x004","D18.000x005","D18.006","D44.700","D44.702","D86.800x005+I41.8*","E03.900x004+I43.8*","E05.900x004+I43.8*","E05.903+I43.8*","E10.400x311+G99.0*","E10.502+I79.2*","E11.400x311+G99.0*","E11.500x021+I79.2*","E11.501+I79.2*","E12.500","E74.008+I43.1*","E76.300x002+I52.8*","E85.416+I43.1*","I01.000","I01.100","I01.200","I01.800x001","I01.900","I02.000x001","I09.000","I09.200","I09.200x001","I09.200x003","I09.200x004","I09.900","I09.900x002","I25.300x006","I25.300x007","I25.300x008","I25.300x009","I25.300x010","I25.300x011","I25.300x012","I25.300x013","I25.301","I25.302","I26.001","I27.100","I27.900","I27.900x002","I28.000x003","I28.100","I28.800x005","I28.800x007","I28.804","I28.900x001","I30.000","I30.100","I30.100x005","I30.100x006","I30.100x007","I30.100x008","I30.101","I30.102","I30.103","I30.801","I30.900","I30.900x001","I30.900x003","I31.000","I31.000x002","I31.001","I31.100","I31.100x001","I31.101","I31.200x001","I31.300","I31.300x005","I31.301","I31.302","I31.800x001","I31.800x003","I31.900x008","I31.900x009","I31.900x010","I31.901","I31.902","I31.903","I31.904","I40.000x003","I40.000x004","I40.000x005","I40.000x006","I40.000x007","I40.001","I40.002","I40.100","I40.800x001","I40.800x002","I40.800x003","I40.900","I42.300","I42.301","I42.800x001","I42.801","I50.906","I51.000x001","I51.001","I51.301","I51.302","I51.303","I51.304","I51.400","I51.400x005","I51.400x006","I51.401","I51.402","I51.403","I51.403","I51.404","I51.500x002","I51.501","I51.502","I51.700","I51.700x003","I51.700x004","I51.700x006","I51.700x007","I51.700x009","I51.700x014","I51.700x015","I51.701","I51.702","I51.703","I51.704","I51.705","I51.706","I51.707","I51.708","I51.709","I51.800x004","I51.800x005","I51.800x006","I51.801","I51.802","I51.900","I51.900x001","I51.900x002","I51.900x003","I51.901","I51.903","I78.000","I78.101","I78.102","I78.801","I78.803","I78.900","I89.001","I95.000","I95.200","I95.800x001","I95.900","I97.000","I97.000x002","I97.001","I97.800x001","I97.800x002","I97.800x004","I97.800x005","I97.800x006","I97.800x008","I97.800x009","I97.800x010","I97.800x011","I97.800x013","I97.800x014","I97.800x015","I97.800x018","I97.801","I97.900","I99.x01","J09.x03+I41.1*","J10.800x003+I41.1*","J10.802+I41.1*","J11.801+I41.1*","J94.000","M05.200","M05.200x092","M05.302+I43.8*","M05.304+I52.8*","M05.305+I32.8*","M05.306+I41.8*","M05.307+I39.8*","M10.004+I43.8*","M32.105+I32.8*","M32.109+I39.8*","M34.800x009+I52.8*","Q27.001","Q27.300x009","Q27.800x020","Q27.800x034","Q27.800x035","Q27.800x037","Q27.803","Q27.806","Q27.809","Q27.811","Q27.815","Q28.900","Q85.900x048","R01.000","R01.100","R01.200x003","R03.100","R09.800x081","R09.800x082","R93.100x002","R93.101","R93.102","R93.103","R94.300","R94.300x003","R94.300x007","R94.300x010","R94.301","R94.303","R94.304","R94.305","R94.306","R94.307","S09.000x001","S15.700x001","S25.400","S25.500","S25.700","S25.900","S26.000x001","S26.000x002","S26.010","S26.800x011","S26.800x021","S26.800x031","S26.800x082","S26.800x083","S26.801","S26.810","S26.811","S26.812","S26.813","S26.900","S26.910","S35.700x001","S35.700x004","S35.701","S35.900x001","S35.901","S35.902","S35.903","S45.700x001","S45.701","S45.800","S45.900x001","S55.700x001","S55.800","S55.900x001","S65.400","S65.500","S65.700x001","S65.800","S65.900x001","S75.700x001","S75.700x002","S75.800","S75.900x001","S75.900x002","S85.700x001","S85.800x001","S85.900x001","S95.700x001","S95.800","S95.900x001","T11.400","T13.400","T70.200x007","T79.101","T80.000","T80.000x001","T81.700x002","T81.700x003","T81.700x004","T81.700x005","T81.700x101","T81.700x102","T81.700x103","T81.700x104","T81.700x105","T81.700x201","T81.700x202","T81.700x203","T81.700x204","T81.700x205","T81.700x301","T81.700x302","T81.700x303","T81.700x304","T81.700x308","T81.700x401","T81.700x402","T81.700x403","T81.700x404","T81.700x405","T81.703","T82.000x002","T82.002","T82.100","T82.100x002","T82.100x003","T82.100x005","T82.100x006","T82.100x007","T82.100x008","T82.100x009","T82.100x010","T82.100x011","T82.100x012","T82.100x013","T82.100x014","T82.100x015","T82.101","T82.102","T82.103","T82.300","T82.301","T82.302","T82.303","T82.400","T82.401","T82.500x001","T82.500x002","T82.500x003","T82.500x003","T82.501","T82.502","T82.503","T82.504","T82.600","T82.600x001","T82.601","T82.700","T82.704","T82.800x001","T82.800x003","T82.800x004","T82.800x005","T82.800x006","T82.800x008","T82.800x009","T82.800x101","T82.800x102","T82.800x103","T82.800x104","T82.800x105","T82.800x106","T82.800x201","T82.800x202","T82.800x203","T82.800x204","T82.800x205","T82.800x206","T82.800x207","T82.800x208","T82.800x301","T82.800x302","T82.800x303","T82.800x304","T82.800x305","T82.800x306","T82.800x307","T82.800x308","T82.800x409","T82.800x410","T82.800x411","T82.811","T82.814","T82.900x001","T82.900x002","T82.901","T82.903","T82.904","T86.200x001","T86.200x002","T86.300x001","T86.300x002","Z03.500x001","Z03.501","Z52.700"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合FZ1入组条件，匹配规则：主诊断匹配')
    
    if MDCF_DRG.FZ11_group(record):
      return 'FZ11'

    if MDCF_DRG.FZ13_group(record):
      return 'FZ13'

    if MDCF_DRG.FZ15_group(record):
      return 'FZ15'

    if MDCF_DRG.FZ17_group(record):
      return 'FZ17'

    return 'FZ1'
  else:
    return ''

