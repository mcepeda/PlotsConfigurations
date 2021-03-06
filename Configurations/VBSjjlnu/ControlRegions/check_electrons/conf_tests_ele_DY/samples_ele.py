import os
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *

samples={}

def nanoGetSampleFiles(inputDir, sample):
    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')


skim=''
##############################################
###### Tree Directory according to site ######
##############################################

SITE=os.uname()[1]
xrootdPath=''
if    'iihe' in SITE :
  xrootdPath  = 'dcap://maite.iihe.ac.be/'
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/'
elif  'cern' in SITE :
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'

directory = treeBaseDir+'/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6/'

################################################
############ NUMBER OF LEPTONS #################
################################################

Nlep='2'
#Nlep='3'
#Nlep='4'

################################################
############### Lepton WP ######################
################################################

eleWP='mvaFall17V1Iso_WP90' 
muWP='cut_Tight_HWWW'

LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP


################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight      = 'XSWeight'
SFweight      = 'puWeight*\
                  TriggerEffWeight_sngEl*\
                  Lepton_RecoSF[0]*\
                  Lepton_RecoSF[1]*\
                  EMTFbug_veto  *'+LepWPweight+'*'+LepWPCut
GenLepMatch   = 'PromptGenLepMatch'+Nlep+'l' # is this a real FIXME (dario)? "FIXME change when we use real fakes"


################################################
############## FAKE WEIGHTS ####################
################################################

if Nlep == '2' :
  fakeW = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP
else:
  fakeW = 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l'


################################################
############### B-Tag  WP ######################
################################################

# Definitions in aliases.py

# FIXME (dario) is it not so necessary in DY?
SFweight += '*btagSF'

################################################
############### AD Hoc### ######################
################################################

# SFweight += '*nvtx_reweighting'

################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
            ['A','Run2018A-Nano25Oct2019-v1'] ,
            ['B','Run2018B-Nano25Oct2019-v1'] ,
            ['C','Run2018C-Nano25Oct2019-v1'] ,
            ['D','Run2018D-Nano25Oct2019_ver2-v1'] ,
          ]

DataSets = ['EGamma'] # FIXME (dario): different dataset in 2018? 

DataTrig = {
            #'MuonEG'         : 'Trigger_ElMu' ,
            # 'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
            # 'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
            'EGamma'         : 'Trigger_sngEl' ,
           }


###########################################
#############  BACKGROUNDS  ###############
###########################################

ptllDYW_NLO = '(0.87*(gen_ptll<10)+(0.379119+0.099744*gen_ptll-0.00487351*gen_ptll**2+9.19509e-05*gen_ptll**3-6.0212e-07*gen_ptll**4)*(gen_ptll>=10 && gen_ptll<45)+(9.12137e-01+1.11957e-04*gen_ptll-3.15325e-06*gen_ptll**2-4.29708e-09*gen_ptll**3+3.35791e-11*gen_ptll**4)*(gen_ptll>=45 && gen_ptll<200) + 1*(gen_ptll>200))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'

useDYtt = False

files=[]
if useDYtt:
  files = nanoGetSampleFiles(directory, 'DYJetsToTT_MuEle_M-50') + \
          nanoGetSampleFiles(directory, 'DYJetsToLL_M-10to50-LO')

else:
  files = nanoGetSampleFiles(directory, 'DYJetsToLL_M-50') + \
          nanoGetSampleFiles(directory, 'DYJetsToLL_M-10to50-LO')


samples['DY'] = {
    'name': files,
    'weight': XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
                                     Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )',
    'FilesPerJob': 3,
}
addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50',ptllDYW_NLO)
addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_NLO)
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)



############ Top ############


samples['top'] = {    'name'   :   getSampleFiles(directory,'TTTo2L2Nu',False,'nanoLatino_') 
                                 + getSampleFiles(directory,'ST_s-channel_ext1',False,'nanoLatino_') # FIXME (dario) whyt is this using _ext ?
                                 + getSampleFiles(directory,'ST_t-channel_antitop',False,'nanoLatino_') 
                                 + getSampleFiles(directory,'ST_t-channel_top',False,'nanoLatino_') 
                                 + getSampleFiles(directory,'ST_tW_antitop_ext1',False,'nanoLatino_') # FIXME (dario) whyt is this using _ext ?
                                 + getSampleFiles(directory,'ST_tW_top_ext1',False,'nanoLatino_') , # FIXME (dario) whyt is this using _ext ?
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC +"*Top_pTrw" ,
                     'FilesPerJob' : 3,
                 }

#addSampleWeight(samples,'top','TTTo2L2Nu',Top_pTrw)

############ WW ############

samples['WW'] = {    'name'   :   getSampleFiles(directory,'WWTo2L2Nu',False,'nanoLatino_') ,
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*nllW' ,
                 }

samples['ggWW']  = {  'name'   :   getSampleFiles(directory,'GluGluToWWToENEN',False,'nanoLatino_')
                                 + getSampleFiles(directory,'GluGluToWWToENMN',False,'nanoLatino_') 
                                 + getSampleFiles(directory,'GluGluToWWToENTN',False,'nanoLatino_')
                                 + getSampleFiles(directory,'GluGluToWWToMNEN',False,'nanoLatino_')
                                 + getSampleFiles(directory,'GluGluToWWToMNMN',False,'nanoLatino_')
                                 + getSampleFiles(directory,'GluGluToWWToMNTN',False,'nanoLatino_')
                                 + getSampleFiles(directory,'GluGluToWWToTNEN',False,'nanoLatino_')
                                 + getSampleFiles(directory,'GluGluToWWToTNMN',False,'nanoLatino_')
                                 + getSampleFiles(directory,'GluGluToWWToTNTN',False,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                   }


############ Vg ############

samples['Vg']  = {  'name'   :   getSampleFiles(directory,'Wg_MADGRAPHMLM',False,'nanoLatino_')
                               + getSampleFiles(directory,'Zg',False,'nanoLatino_'), # FIXME `Zg` or `ZGToLLG` ?
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC + '* (!(Gen_ZGstar_mass > 0 && Gen_ZGstar_MomId == 22 ))',
                    'FilesPerJob': 6,
                  }


############ VgS ############

samples['VgS']  =  {  'name'   :   getSampleFiles(directory,'Wg_MADGRAPHMLM',False,'nanoLatino_')
                                 + getSampleFiles(directory,'Zg',False,'nanoLatino_')
                                 + getSampleFiles(directory,'WZTo3LNu_mllmin01',False,'nanoLatino_'), # FIXME (dario) `Zg` or `ZGToLLG` ? # (dario) FIXME consider WZTo3LNu_mllmin01 ?
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                      'FilesPerJob' : 20 ,
                   }
addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM',    '(Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples,'VgS','Zg',                '(Gen_ZGstar_mass >0)') # FIXME `Zg` or `ZGToLLG` ?
addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass>=0.1 || Gen_ZGstar_mass<0)')

############ VZ ############

#FIXME Add normalization k-factor
# Is this a true FIXME? (dario)
samples['VZ']  = {  'name'   :   getSampleFiles(directory,'ZZTo2L2Nu_ext1',False,'nanoLatino_')
                               + getSampleFiles(directory,'ZZTo2L2Q',False,'nanoLatino_')
                               + getSampleFiles(directory,'ZZTo4L_ext1',False,'nanoLatino_') 
                               + getSampleFiles(directory,'WZTo2L2Q',False,'nanoLatino_'),
                    'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                    'FilesPerJob' : 6,
                 }


############ VVV ############

samples['VVV']  = {  'name'   :   getSampleFiles(directory,'ZZZ',False,'nanoLatino_')
                                + getSampleFiles(directory,'WZZ',False,'nanoLatino_')
                                + getSampleFiles(directory,'WWZ',False,'nanoLatino_')
                                + getSampleFiles(directory,'WWW',False,'nanoLatino_'),
                                #+ getSampleFiles(directory,'WWG',False,'nanoLatino_'), #should this be included? or is it already taken into account in the WW sample?
                    'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                    'FilesPerJob' : 8,
                  }

###########################################
################## FAKE ###################
###########################################

# samples['Fake_ee']  = {   'name': [ ] ,
#                          'weight' : METFilter_DATA+'*'+fakeW+'*(abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==11)',              #   weight/cut 
#                          'weights' : [ ] ,
#                          'isData': ['all'],
#                          'FilesPerJob' : 15 ,
#                       }

# samples['Fake_mm']  = {   'name': [ ] ,
#                          'weight' : METFilter_DATA+'*'+fakeW+'*(abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==13)',              #   weight/cut 
#                          'weights' : [ ] ,
#                          'isData': ['all'],
#                          'FilesPerJob' : 15 ,
#                       }

# for Run in DataRun :
#         directory = treeBaseDir+'Run2018_102X_nAODv5_Full2018v5/DATAl1loose2018v5__l2loose__fakeW/'
#         for DataSet in DataSets :
#                 FileTarget = getSampleFiles(directory,DataSet+'_'+Run[1],True,'nanoLatino_')
#                 for iFile in FileTarget:
#                         samples['Fake_ee']['name'].append(iFile)
#                         samples['Fake_ee']['weights'].append(DataTrig[DataSet])
#                         samples['Fake_mm']['name'].append(iFile)
#                         samples['Fake_mm']['weights'].append(DataTrig[DataSet])


samples['Fake']  = {   'name': [ ] ,
                         'weight' : METFilter_DATA+'*'+fakeW,              #   weight/cut 
                         'weights' : [ ] ,
                         'isData': ['all'],
                         'FilesPerJob' : 20 ,
                      }

for Run in DataRun :
        directory = treeBaseDir+'Run2018_102X_nAODv6_Full2018v6/DATAl1loose2018v6__l2loose__fakeW/'
        for DataSet in DataSets :
                FileTarget = getSampleFiles(directory,DataSet+'_'+Run[1],True,'nanoLatino_')
                for iFile in FileTarget:
                        samples['Fake']['name'].append(iFile)
                        samples['Fake']['weights'].append(DataTrig[DataSet])

###########################################
################## DATA ###################
###########################################

samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 20,
                  }

for Run in DataRun :
        directory = treeBaseDir+'Run2018_102X_nAODv6_Full2018v6/DATAl1loose2018v6__l2loose__l2tightOR2018v6/'
        for DataSet in DataSets :
                FileTarget = getSampleFiles(directory,DataSet+'_'+Run[1],True,'nanoLatino_')
                for iFile in FileTarget:
                        #print(iFile)
                        samples['DATA']['name'].append(iFile)
                        samples['DATA']['weights'].append(DataTrig[DataSet])



#samples= { k:v for k,v in samples.items() if k in ["Vg"]}