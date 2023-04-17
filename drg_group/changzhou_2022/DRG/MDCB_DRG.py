from drg_group.changzhou_2022.Base import has_mcc,has_cc,intersect
def BT10_group(record):
    return record.age<=17
def BU20_group(record):
    return record.age<=17
def BY10_group(record):
    return record.age<=17
def BZ10_group(record):
    return record.age<=17
def BB19_group(record):
  return True
def BB29_group(record):
  return True
def BC19_group(record):
  return True
def BC29_group(record):
  return True
def BD19_group(record):
  return True
def BD29_group(record):
  return True
def BE19_group(record):
  return True
def BE29_group(record):
  return True
def BL19_group(record):
  return True
def BU29_group(record):
  return True
def BU39_group(record):
  return True
def BV29_group(record):
  return True
def BV39_group(record):
  return True
def BW29_group(record):
  return True
def BX19_group(record):
  return True
def BX29_group(record):
  return True
def BR17_group(record):
  return record.inHospitalTime<5 and record.leavingType in ['2','5']
def BR27_group(record):
  return record.inHospitalTime<5 and record.leavingType in ['2','5']
def BY27_group(record):
  return record.inHospitalTime<5 and record.leavingType in ['2','5']
def BV12_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:]) and record.age<=17
def BJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BM11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BR21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BT21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BW11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BY11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BY21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BY31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BV14_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:]) and record.age<=17
def BJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BM13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BR23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BT13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BT23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BV13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BW13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BY13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BY23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BY33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BV16_group(record):
  return record.age<=17
def BJ15_group(record):
  return True
def BM15_group(record):
  return True
def BR15_group(record):
  return True
def BR25_group(record):
  return True
def BS15_group(record):
  return True
def BT15_group(record):
  return True
def BT25_group(record):
  return True
def BU15_group(record):
  return True
def BV15_group(record):
  return True
def BW15_group(record):
  return True
def BY15_group(record):
  return True
def BY25_group(record):
  return True
def BY35_group(record):
  return True
def BZ15_group(record):
  return True

