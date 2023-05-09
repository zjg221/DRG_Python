from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCV_DRG

def group(record):
  adrg_zd=["S00.102","S09.700","S21.200x001","S21.901","S30.201","S31.000x005","S31.003","S31.004","S31.102","S38.101","S39.900x004","S39.907","S41.100","S47.x01","S49.900x001","S51.000","S51.800x011","S57.900","S58.100x001","S61.000x001","S61.000x002","S61.100x001","S61.100x002","S61.800x012","S61.800x022","S61.800x081","S61.900","S61.900x002","S67.000x001","S67.000x003","S67.001","S67.800x003","S67.801","S68.000x002","S68.100x002","S69.900x002","S69.900x003","S69.900x004","S71.100","S77.100","S79.900x001","S81.000","S81.700","S81.800x011","S81.900","S87.801","S91.000","S91.100","S91.200","S91.300x002","S91.300x813","S91.700x002","S91.700x003","S97.000","S97.100","S97.801","S98.100x001","S99.700x001","S99.900x001","T01.000x001","T01.903","T02.400x001","T02.500x001","T02.600x001","T04.400x001","T06.501","T07.x00","T11.100","T13.100","T78.101","T78.200","T78.300","T78.301","T78.400x002","T88.601"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合VR1入组条件，匹配规则：主诊断匹配')
    
    if MDCV_DRG.VR19_group(record):
      return 'VR19'

    return 'VR1'
  else:
    return ''
