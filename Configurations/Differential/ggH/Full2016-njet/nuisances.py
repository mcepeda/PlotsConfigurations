
# nuisances

#nuisances = {}

# name of samples here must match keys in samples.py 

################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity

nuisances['lumi']  = {
               'name'  : 'lumi_13TeV_2016',
               'samples'  : {
                   #'DY'       : '1.025',    |
                   #'top'      : '1.025',    | These 3 backgrounds are data driven, no need to include the luminosity uncertainty
                   #'WW'       : '1.025',    |
                   'ggWW'     : '1.025',
                   'Vg'       : '1.025',
                   'VgS'      : '1.025',
                   'WZgS_L'   : '1.025',
                   'WZgS_H'   : '1.025',
                   'VZ'       : '1.025',
                   'VVV'      : '1.025',
                   'ggH_hww'  : '1.025',
                   'qqH_hww'  : '1.025',
                   'ZH_hww'   : '1.025',
                   'ggZH_hww' : '1.025',
                   'WH_hww'   : '1.025',
                   'bbH_hww'  : '1.025',
                   'ttH_hww'  : '1.025',
                   'ggH_htt'  : '1.025',
                   'qqH_htt'  : '1.025',
                   'ZH_htt'   : '1.025',
                   'WH_htt'   : '1.025',
                   'H_htt'    : '1.025',
                   #
                   'ggH_hww_0j_fid'   : '1.025',
                   'ggH_hww_1j_fid'   : '1.025',
                   'ggH_hww_2j_fid'   : '1.025',
                   'ggH_hww_3j_fid'   : '1.025',
                   'ggH_hww_4j_fid'   : '1.025',
                   'ggH_hww_0j_nonfid'   : '1.025',
                   'ggH_hww_1j_nonfid'   : '1.025',
                   'ggH_hww_2j_nonfid'   : '1.025',
                   'ggH_hww_3j_nonfid'   : '1.025', 
                   'ggH_hww_4j_nonfid'   : '1.025',
                   #
                   'qqH_hww_0j_fid'    : '1.025',
                   'qqH_hww_1j_fid'    : '1.025',
                   'qqH_hww_2j_fid'    : '1.025',
                   'qqH_hww_3j_fid'    : '1.025',
                   'qqH_hww_4j_fid'    : '1.025',
                   'qqH_hww_0j_nonfid'    : '1.025',
                   'qqH_hww_1j_nonfid'    : '1.025',
                   'qqH_hww_2j_nonfid'    : '1.025',
                   'qqH_hww_3j_nonfid'    : '1.025',
                   'qqH_hww_4j_nonfid'    : '1.025',
                   # 
                   'ZH_hww_0j_fid'           : '1.025',
                   'ZH_hww_1j_fid'           : '1.025',
                   'ZH_hww_2j_fid'           : '1.025',
                   'ZH_hww_3j_fid'           : '1.025',
                   'ZH_hww_4j_fid'           : '1.025',
                   'ZH_hww_0j_nonfid'           : '1.025',
                   'ZH_hww_1j_nonfid'           : '1.025',
                   'ZH_hww_2j_nonfid'           : '1.025',
                   'ZH_hww_3j_nonfid'           : '1.025',
                   'ZH_hww_4j_nonfid'           : '1.025',
                   #
                   'ggZH_hww'         : '1.025',
                   # 
                   'WH_hww_0j_fid'           : '1.025',
                   'WH_hww_1j_fid'           : '1.025',
                   'WH_hww_2j_fid'           : '1.025',
                   'WH_hww_3j_fid'           : '1.025',
                   'WH_hww_4j_fid'           : '1.025',
                   'WH_hww_0j_nonfid'           : '1.025',
                   'WH_hww_1j_nonfid'           : '1.025',
                   'WH_hww_2j_nonfid'           : '1.025',
                   'WH_hww_3j_nonfid'           : '1.025',
                   'WH_hww_4j_nonfid'           : '1.025',
                   #
                   'XH_hww_0j_fid'           : '1.025',
                   'XH_hww_1j_fid'           : '1.025',
                   'XH_hww_2j_fid'           : '1.025',
                   'XH_hww_3j_fid'           : '1.025',
                   'XH_hww_0j_nonfid'           : '1.025',
                   'XH_hww_1j_nonfid'           : '1.025',
                   'XH_hww_2j_nonfid'           : '1.025',
                   'XH_hww_3j_nonfid'           : '1.025',
                   'XH_hww_4j_nonfid'           : '1.025',
                   #
                   'bbH_hww'          : '1.025',
                   'ttH_hww'          : '1.025',
                   #
                   'ggH_htt'          : '1.025',
                   #
                   'qqH_htt'   				: '1.025',
                   # 
                   'ZH_htt'           : '1.025',
                   # 
                   'WH_htt'           : '1.025', 
                   },
               'type'  : 'lnN',
              }

#### FAKES

if Nlep == '2' :
  # already divided by central values in formulas !
  fakeW_EleUp       = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp'
  fakeW_EleDown     = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown'
  fakeW_MuUp        = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp'
  fakeW_MuDown      = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown'
  fakeW_statEleUp   = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp'
  fakeW_statEleDown = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown'
  fakeW_statMuUp    = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp'
  fakeW_statMuDown  = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown'

else:
  fakeW_EleUp       = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lElUp       / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_EleDown     = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lElDown     / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_MuUp        = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lMuUp       / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_MuDown      = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lMuDown     / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_statEleUp   = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatElUp   / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_statEleDown = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatElDown / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_statMuUp    = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatMuUp   / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_statMuDown  = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatMuDown / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'

#nuisances['fake_syst']  = {
#               'name'  : 'fake_syst',
#               'type'  : 'lnN',
#               'samples'  : {
#                             'Fake' : '1.30',
#                             },
#}

nuisances['fake_syst_em']  = {
               'name'  : 'CMS_hwwem_fake_syst_2016',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake_em' : '1.30',
                             },
               }

nuisances['fake_syst_me']  = {
               'name'  : 'CMS_hwwme_fake_syst_2016',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake_me' : '1.30',
                             },
               }

nuisances['fake_ele']  = {
                'name'  : 'hww_fake_ele_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'     : [ fakeW_EleUp , fakeW_EleDown ],
                              'Fake_me'     : [ fakeW_EleUp , fakeW_EleDown ],
                             },
}

nuisances['fake_ele_stat']  = {
                'name'  : 'hww_fake_ele_stat_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'      : [ fakeW_statEleUp , fakeW_statEleDown ],
                              'Fake_me'      : [ fakeW_statEleUp , fakeW_statEleDown ],
                             },
}

nuisances['fake_mu']  = {
                'name'  : 'hww_fake_mu_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'     : [ fakeW_MuUp , fakeW_MuDown ],
                              'Fake_me'     : [ fakeW_MuUp , fakeW_MuDown ],
                             },
}


nuisances['fake_mu_stat']  = {
                'name'  : 'hww_fake_mu_stat_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'     : [ fakeW_statMuUp , fakeW_statMuDown ],
                              'Fake_me'     : [ fakeW_statMuUp , fakeW_statMuDown ],
                             },
}

##### B-tagger

nuisances['btagbc']  = {
                'name'  : 'btag_heavy_2016',
                'kind'  : 'weight',
               'type'  : 'shape',
                'samples'  : {
                   'DY'      					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'WW'      					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ggWW'    					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'VVV'     					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'VZ'      					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'WZgS_L'   				 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'WZgS_H'  				 	 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'top'     					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'Vg'      					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'VgS'     					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ggH_hww' 					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'qqH_hww' 					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'WH_hww_0j_fid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'WH_hww_1j_fid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'WH_hww_2j_fid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'WH_hww_3j_fid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'WH_hww_4j_fid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'WH_hww_0j_nonfid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'WH_hww_1j_nonfid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'WH_hww_2j_nonfid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'WH_hww_3j_nonfid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'WH_hww_4j_nonfid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ZH_hww_0j_fid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ZH_hww_1j_fid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ZH_hww_2j_fid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ZH_hww_3j_fid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ZH_hww_4j_fid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ZH_hww_0j_nonfid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ZH_hww_1j_nonfid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ZH_hww_2j_nonfid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ZH_hww_3j_nonfid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ZH_hww_4j_nonfid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   #
#                   'XH_hww_0j_fid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
#                   'XH_hww_1j_fid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
#                   'XH_hww_2j_fid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
#                   'XH_hww_3j_fid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
#                   'XH_hww_4j_fid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
#                   'XH_hww_0j_nonfid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
#                   'XH_hww_1j_nonfid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
#                   'XH_hww_2j_nonfid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
#                   'XH_hww_3j_nonfid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
#                   'XH_hww_4j_nonfid'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   #
                   'H_htt'   					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'bbH_hww' 					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ttH_hww' 					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ggH_htt'	 				 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],  
                   'qqH_htt' 					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ZH_htt'  					 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'WH_htt'  				 	 : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   #
                   'ggH_hww_0j_fid'    : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ggH_hww_1j_fid'    : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ggH_hww_2j_fid'    : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ggH_hww_3j_fid'    : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ggH_hww_4j_fid'    : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ggH_hww_0j_nonfid' : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ggH_hww_1j_nonfid' : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ggH_hww_2j_nonfid' : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ggH_hww_3j_nonfid' : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ggH_hww_4j_nonfid' : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'], 
                   #
                   'qqH_hww_0j_fid'    : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'qqH_hww_1j_fid'    : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'qqH_hww_2j_fid'    : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'qqH_hww_3j_fid'    : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'qqH_hww_4j_fid'    : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'qqH_hww_0j_nonfid' : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'qqH_hww_1j_nonfid' : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'qqH_hww_2j_nonfid' : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'qqH_hww_3j_nonfid' : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'qqH_hww_4j_nonfid' : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   # 
                   'ZH_hww'            : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   #
                   'ggZH_hww'          : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   # 
                   'WH_hww'            : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   #
                   'bbH_hww'           : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ttH_hww'           : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   #
                   'ggH_htt'           : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   #
                   'qqH_htt'           : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   # 
                   'ZH_htt'            : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   # 
                   'WH_htt'            : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                }
}

nuisances['btagudsg']  = {
                'name'  : 'btag_light_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'VVV'     : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'VZ'      : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'WZgS_L'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'WZgS_H'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'WW'      : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ggWW'    : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'top'     : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'Vg'      : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'VgS'     : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ggH_hww' : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'qqH_hww' : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'WH_hww_0j_fid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'WH_hww_1j_fid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'WH_hww_2j_fid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'WH_hww_3j_fid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'WH_hww_4j_fid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'WH_hww_0j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'WH_hww_1j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'WH_hww_2j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'WH_hww_3j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'WH_hww_4j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ZH_hww_0j_fid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ZH_hww_1j_fid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ZH_hww_2j_fid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ZH_hww_3j_fid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ZH_hww_4j_fid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ZH_hww_0j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ZH_hww_1j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ZH_hww_2j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ZH_hww_3j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ZH_hww_4j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   #
#                   'XH_hww_0j_fid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
#                   'XH_hww_1j_fid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
#                   'XH_hww_2j_fid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
#                   'XH_hww_3j_fid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
#                   'XH_hww_4j_fid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
#                   'XH_hww_0j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
#                   'XH_hww_1j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
#                   'XH_hww_2j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
#                   'XH_hww_3j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
#                   'XH_hww_4j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   #
                   'bbH_hww' : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ttH_hww' : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'H_htt'   : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ggH_htt' : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'qqH_htt' : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ZH_htt'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'WH_htt'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   #
                   'ggH_hww_0j_fid'   	: ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ggH_hww_1j_fid'   	: ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ggH_hww_2j_fid'   	: ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ggH_hww_3j_fid'   	: ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ggH_hww_4j_fid'   	: ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ggH_hww_0j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ggH_hww_1j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ggH_hww_2j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ggH_hww_3j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ggH_hww_4j_nonfid'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   #
                   'qqH_hww_0j_fid'  	 : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'qqH_hww_1j_fid'    : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'qqH_hww_2j_fid'    : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'qqH_hww_3j_fid'    : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'qqH_hww_4j_fid'    : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'qqH_hww_0j_nonfid' : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'qqH_hww_1j_nonfid' : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'qqH_hww_2j_nonfid' : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'qqH_hww_3j_nonfid' : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'qqH_hww_4j_nonfid' : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   # 
                   'ZH_hww'           : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   #
                   'ggZH_hww'         : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   # 
                   'WH_hww'           : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   #
                   'bbH_hww'          : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ttH_hww'          : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   #
                   'ggH_htt'          : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   #
                   'qqH_htt'          : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   # 
                   'ZH_htt'           : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   # 
                   'WH_htt'           : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                }
}

##### Trigger Efficiency

if   Nlep == '2' : trig_syst = ['(effTrigW_Up)/(effTrigW)', '(effTrigW_Down)/(effTrigW)']
elif Nlep == '3' : trig_syst = ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)']
elif Nlep == '4' : trig_syst = ['(effTrigW4l_Up)/(effTrigW4l)', '(effTrigW3l_Down)/(effTrigW4l)']

nuisances['trigg']  = {
                'name'  : 'hww_trigger_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : trig_syst ,
                   'VVV'     : trig_syst ,
                   'VZ'      : trig_syst ,
                   'WZgS_L'  : trig_syst ,
                   'WZgS_H'  : trig_syst ,
                   'ggWW'    : trig_syst ,
                   'WW'      : trig_syst ,
                   'top'     : trig_syst ,
                   'Vg'      : trig_syst ,
                   'VgS'     : trig_syst ,
                   'ggH_hww' : trig_syst ,
                   'qqH_hww' : trig_syst ,
                   'WH_hww_0j_fid'  : trig_syst ,
                   'WH_hww_1j_fid'  : trig_syst ,
                   'WH_hww_2j_fid'  : trig_syst ,
                   'WH_hww_3j_fid'  : trig_syst ,
                   'WH_hww_4j_fid'  : trig_syst ,
                   'WH_hww_0j_nonfid'  : trig_syst ,
                   'WH_hww_1j_nonfid'  : trig_syst ,
                   'WH_hww_2j_nonfid'  : trig_syst ,
                   'WH_hww_3j_nonfid'  : trig_syst ,
                   'WH_hww_4j_nonfid'  : trig_syst ,
                   'ZH_hww_0j_fid'  : trig_syst ,
                   'ZH_hww_1j_fid'  : trig_syst ,
                   'ZH_hww_2j_fid'  : trig_syst ,
                   'ZH_hww_3j_fid'  : trig_syst ,
                   'ZH_hww_4j_fid'  : trig_syst ,
                   'ZH_hww_0j_nonfid'  : trig_syst ,
                   'ZH_hww_1j_nonfid'  : trig_syst ,
                   'ZH_hww_2j_nonfid'  : trig_syst ,
                   'ZH_hww_3j_nonfid'  : trig_syst ,
                   'ZH_hww_4j_nonfid'  : trig_syst ,
                   #
#                   'XH_hww_0j_fid'  : trig_syst ,
#                   'XH_hww_1j_fid'  : trig_syst ,
#                   'XH_hww_2j_fid'  : trig_syst ,
#                   'XH_hww_3j_fid'  : trig_syst ,
#                   'XH_hww_4j_fid'  : trig_syst ,
#                   'XH_hww_0j_nonfid'  : trig_syst ,
#                   'XH_hww_1j_nonfid'  : trig_syst ,
#                   'XH_hww_2j_nonfid'  : trig_syst ,
#                   'XH_hww_3j_nonfid'  : trig_syst ,
#                   'XH_hww_4j_nonfid'  : trig_syst ,
                   #
                   'ggZH_hww': trig_syst ,
                   'bbH_hww' : trig_syst ,
                   'ttH_hww' : trig_syst ,
                   'H_htt'   : trig_syst ,
                   'ggH_htt' : trig_syst ,
                   'qqH_htt' : trig_syst ,
                   'ZH_htt'  : trig_syst ,
                   'WH_htt'  : trig_syst ,
                   #
                   'ggH_hww_0j_fid'    : trig_syst ,
                   'ggH_hww_1j_fid'    : trig_syst ,
                   'ggH_hww_2j_fid'    : trig_syst ,
                   'ggH_hww_3j_fid'    : trig_syst ,
                   'ggH_hww_4j_fid'    : trig_syst ,
                   'ggH_hww_0j_nonfid' : trig_syst ,
                   'ggH_hww_1j_nonfid' : trig_syst ,
                   'ggH_hww_2j_nonfid' : trig_syst ,
                   'ggH_hww_3j_nonfid' : trig_syst ,
                   'ggH_hww_4j_nonfid' : trig_syst , 
                   #
                   'qqH_hww_0j_fid'          : trig_syst ,
                   'qqH_hww_1j_fid'          : trig_syst ,
                   'qqH_hww_2j_fid'          : trig_syst ,
                   'qqH_hww_3j_fid'          : trig_syst ,
                   'qqH_hww_4j_fid'          : trig_syst ,
                   'qqH_hww_0j_nonfid'       : trig_syst ,
                   'qqH_hww_1j_nonfid'       : trig_syst ,
                   'qqH_hww_2j_nonfid'       : trig_syst ,
                   'qqH_hww_3j_nonfid'       : trig_syst ,
                   'qqH_hww_4j_nonfid'       : trig_syst ,
                   # 
                   #'ZH_hww'           : trig_syst ,
                   #
                   'ggZH_hww'         : trig_syst ,
                   # 
                   #'WH_hww'           : trig_syst ,
                   #
                   'bbH_hww'          : trig_syst ,
                   'ttH_hww'          : trig_syst ,
                   #
                   #'ggH_htt'          : trig_syst ,
                   #
                   #'qqH_htt'          : trig_syst ,
                   # 
                   #'ZH_htt'           : trig_syst ,
                   # 
                   #'WH_htt'           : trig_syst ,
                },
}

##### Electron Efficiency and energy scale

id_syst_ele = [ 'LepSF'+Nlep+'l__ele_'+eleWP+'__Up' , 'LepSF'+Nlep+'l__ele_'+eleWP+'__Do' ]

nuisances['eff_e']  = {
                'name'  : 'eff_e_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : id_syst_ele ,
                   'VVV'     : id_syst_ele ,
                   'VZ'      : id_syst_ele ,
                   'WZgS_L'  : id_syst_ele ,
                   'WZgS_H'  : id_syst_ele ,
                   'ggWW'    : id_syst_ele ,
                   'WW'      : id_syst_ele ,
                   'top'     : id_syst_ele ,
                   'Vg'      : id_syst_ele ,
                   'VgS'     : id_syst_ele ,
                   'ggH_hww' : id_syst_ele ,
                   'qqH_hww' : id_syst_ele ,
                   'WH_hww'  : id_syst_ele ,
                   'ZH_hww'  : id_syst_ele ,
                   'ggZH_hww': id_syst_ele ,
                   'bbH_hww' : id_syst_ele ,
                   'ttH_hww' : id_syst_ele ,
                   'H_htt'   : id_syst_ele ,
                   'ggH_htt' : id_syst_ele ,
                   'qqH_htt' : id_syst_ele ,
                   'ZH_htt'  : id_syst_ele ,
                   'WH_htt'  : id_syst_ele ,
                   #
                   'ggH_hww_0j_fid'   : id_syst_ele ,
                   'ggH_hww_1j_fid'   : id_syst_ele ,
                   'ggH_hww_2j_fid'   : id_syst_ele ,
                   'ggH_hww_3j_fid'   : id_syst_ele ,
                   'ggH_hww_4j_fid'   : id_syst_ele ,
                   'ggH_hww_0j_nonfid': id_syst_ele ,
                   'ggH_hww_1j_nonfid': id_syst_ele ,
                   'ggH_hww_2j_nonfid': id_syst_ele ,
                   'ggH_hww_3j_nonfid': id_syst_ele ,
                   'ggH_hww_4j_nonfid': id_syst_ele ,
                   #
                   'qqH_hww_0j_fid'   : id_syst_ele ,
                   'qqH_hww_1j_fid'   : id_syst_ele ,
                   'qqH_hww_2j_fid'   : id_syst_ele ,
                   'qqH_hww_3j_fid'   : id_syst_ele ,
                   'qqH_hww_4j_fid'   : id_syst_ele ,
                   'qqH_hww_0j_nonfid': id_syst_ele ,
                   'qqH_hww_1j_nonfid': id_syst_ele ,
                   'qqH_hww_2j_nonfid': id_syst_ele ,
                   'qqH_hww_3j_nonfid': id_syst_ele ,
                   'qqH_hww_4j_nonfid': id_syst_ele ,
                   # 
                   'ZH_hww_0j_fid'           : id_syst_ele ,
                   'ZH_hww_1j_fid'           : id_syst_ele ,
                   'ZH_hww_2j_fid'           : id_syst_ele ,
                   'ZH_hww_3j_fid'           : id_syst_ele ,
                   'ZH_hww_4j_fid'           : id_syst_ele ,
                   'ZH_hww_0j_nonfid'           : id_syst_ele ,
                   'ZH_hww_1j_nonfid'           : id_syst_ele ,
                   'ZH_hww_2j_nonfid'           : id_syst_ele ,
                   'ZH_hww_3j_nonfid'           : id_syst_ele ,
                   'ZH_hww_4j_nonfid'           : id_syst_ele ,
                   #
                   'ggZH_hww'         : id_syst_ele ,
                   # 
                   'WH_hww_0j_fid'           : id_syst_ele ,
                   'WH_hww_1j_fid'           : id_syst_ele ,
                   'WH_hww_2j_fid'           : id_syst_ele ,
                   'WH_hww_3j_fid'           : id_syst_ele ,
                   'WH_hww_4j_fid'           : id_syst_ele ,
                   'WH_hww_0j_nonfid'           : id_syst_ele ,
                   'WH_hww_1j_nonfid'           : id_syst_ele ,
                   'WH_hww_2j_nonfid'           : id_syst_ele ,
                   'WH_hww_3j_nonfid'           : id_syst_ele ,
                   'WH_hww_4j_nonfid'           : id_syst_ele ,
                   #
#                   'XH_hww_0j_fid'           : id_syst_ele ,
#                   'XH_hww_1j_fid'           : id_syst_ele ,
#                   'XH_hww_2j_fid'           : id_syst_ele ,
#                   'XH_hww_3j_fid'           : id_syst_ele ,
#                   'XH_hww_4j_fid'           : id_syst_ele ,
#                   'XH_hww_0j_nonfid'           : id_syst_ele ,
#                   'XH_hww_1j_nonfid'           : id_syst_ele ,
#                   'XH_hww_2j_nonfid'           : id_syst_ele ,
#                   'XH_hww_3j_nonfid'           : id_syst_ele ,
#                   'XH_hww_4j_nonfid'           : id_syst_ele ,
                   #
                   'bbH_hww'          : id_syst_ele ,
                   'ttH_hww'          : id_syst_ele ,
                   #
                   'ggH_htt'          : id_syst_ele ,
                   #
                   'qqH_htt'          : id_syst_ele ,
                   # 
                   'ZH_htt'           : id_syst_ele ,
                   # 
                   'WH_htt'           : id_syst_ele , 
                },
}

nuisances['electronpt']  = {
                'name'  : 'scale_e_2016',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['1', '1'],
                   'ggWW'    : ['1', '1'],
                   'WW'      : ['1', '1'],
                   'top'     : ['1', '1'],
                   'VZ'      : ['1', '1'],
                   'WZgS_L'  : ['1', '1'],
                   'WZgS_H'  : ['1', '1'],
                   'VVV'     : ['1', '1'],
                   'Vg'      : ['1', '1'],
                   'VgS'     : ['1', '1'],
                   'ggH_hww ': ['1', '1'],
                   'qqH_hww ': ['1', '1'],
                   'WH_hww_0j_fid'  : ['1', '1'],
                   'WH_hww_1j_fid'  : ['1', '1'],
                   'WH_hww_2j_fid'  : ['1', '1'],
                   'WH_hww_3j_fid'  : ['1', '1'],
                   'WH_hww_4j_fid'  : ['1', '1'],
                   'WH_hww_0j_nonfid'  : ['1', '1'],
                   'WH_hww_1j_nonfid'  : ['1', '1'],
                   'WH_hww_2j_nonfid'  : ['1', '1'],
                   'WH_hww_3j_nonfid'  : ['1', '1'],
                   'WH_hww_4j_nonfid'  : ['1', '1'],
                   'ZH_hww_0j_fid'  : ['1', '1'],
                   'ZH_hww_1j_fid'  : ['1', '1'],
                   'ZH_hww_2j_fid'  : ['1', '1'],
                   'ZH_hww_3j_fid'  : ['1', '1'],
                   'ZH_hww_4j_fid'  : ['1', '1'],
                   'ZH_hww_0j_nonfid'  : ['1', '1'],
                   'ZH_hww_1j_nonfid'  : ['1', '1'],
                   'ZH_hww_2j_nonfid'  : ['1', '1'],
                   'ZH_hww_3j_nonfid'  : ['1', '1'],
                   'ZH_hww_4j_nonfid'  : ['1', '1'],
                   #
#                   'XH_hww_0j_fid'  : ['1', '1'],
#                   'XH_hww_1j_fid'  : ['1', '1'],
#                   'XH_hww_2j_fid'  : ['1', '1'],
#                   'XH_hww_3j_fid'  : ['1', '1'],
#                   'XH_hww_4j_fid'  : ['1', '1'],
#                   'XH_hww_0j_nonfid'  : ['1', '1'],
#                   'XH_hww_1j_nonfid'  : ['1', '1'],
#                   'XH_hww_2j_nonfid'  : ['1', '1'],
#                   'XH_hww_3j_nonfid'  : ['1', '1'],
#                   'XH_hww_4j_nonfid'  : ['1', '1'],
                   #
                   'ggZH_hww': ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'ttH_hww' : ['1', '1'],
                   'H_htt'   : ['1', '1'],
                   'ggH_htt' : ['1', '1'] ,
                   'qqH_htt' : ['1', '1'] ,
                   'ZH_htt'  : ['1', '1'] ,
                   'WH_htt'  : ['1', '1'] ,
                   #
                   'ggH_hww_0j_fid'   : ['1', '1'], 
                   'ggH_hww_1j_fid'   : ['1', '1'],
                   'ggH_hww_2j_fid'   : ['1', '1'],
                   'ggH_hww_3j_fid'   : ['1', '1'],
                   'ggH_hww_4j_fid'   : ['1', '1'], 
                   'ggH_hww_0j_nonfid': ['1', '1'], 
                   'ggH_hww_1j_nonfid': ['1', '1'],
                   'ggH_hww_2j_nonfid': ['1', '1'],
                   'ggH_hww_3j_nonfid': ['1', '1'],
                   'ggH_hww_4j_nonfid': ['1', '1'],
                   #
                   'qqH_hww_0j_fid'   : ['1', '1'],
                   'qqH_hww_1j_fid'   : ['1', '1'],
                   'qqH_hww_2j_fid'   : ['1', '1'],
                   'qqH_hww_3j_fid'   : ['1', '1'],
                   'qqH_hww_4j_fid'   : ['1', '1'],
                   'qqH_hww_0j_nonfid': ['1', '1'],
                   'qqH_hww_1j_nonfid': ['1', '1'],
                   'qqH_hww_2j_nonfid': ['1', '1'],
                   'qqH_hww_3j_nonfid': ['1', '1'],
                   'qqH_hww_4j_nonfid': ['1', '1'],
                   # 
                   'ZH_hww'           : ['1', '1'],
                   #
                   'ggZH_hww'         : ['1', '1'],
                   # 
                   'WH_hww'           : ['1', '1'],
                   #
                   'bbH_hww'          : ['1', '1'],
                   'ttH_hww'          : ['1', '1'],
                   #
                   'ggH_htt'          : ['1', '1'],
                   #
                   'qqH_htt'          : ['1', '1'],
                   # 
                   'ZH_htt'           : ['1', '1'],
                   # 
                   'WH_htt'           : ['1', '1'],
                 },
                'folderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__LepElepTup'+skim,
                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__LepElepTdo'+skim,
}


elePtCor_Syst = [ 'electron_ptW_'+Nlep+'l_Up / electron_ptW_'+Nlep+'l', 'electron_ptW_'+Nlep+'l_Down / electron_ptW_'+Nlep+'l']
nuisances['elePtCor']  = {
                'name'  : 'hww_elePtCor_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'         : elePtCor_Syst ,
                   'ggWW'       : elePtCor_Syst ,
                   'WW'         : elePtCor_Syst ,
                   'top'        : elePtCor_Syst ,
                   'VZ'         : elePtCor_Syst ,
                   'WZgS_L'     : elePtCor_Syst ,
                   'WZgS_H'     : elePtCor_Syst ,
                   'VVV'        : elePtCor_Syst ,
                   'Vg'         : elePtCor_Syst ,
                   'VgS'        : elePtCor_Syst ,
                   'ggH_hww'    : elePtCor_Syst ,
                   'qqH_hww'    : elePtCor_Syst ,
                   'WH_hww_0j_fid'     : elePtCor_Syst ,
                   'WH_hww_1j_fid'     : elePtCor_Syst ,
                   'WH_hww_2j_fid'     : elePtCor_Syst ,
                   'WH_hww_3j_fid'     : elePtCor_Syst ,
                   'WH_hww_4j_fid'     : elePtCor_Syst ,
                   'WH_hww_0j_nonfid'     : elePtCor_Syst ,
                   'WH_hww_1j_nonfid'     : elePtCor_Syst ,
                   'WH_hww_2j_nonfid'     : elePtCor_Syst ,
                   'WH_hww_3j_nonfid'     : elePtCor_Syst ,
                   'WH_hww_4j_nonfid'     : elePtCor_Syst ,
                   'ZH_hww_0j_fid'     : elePtCor_Syst ,
                   'ZH_hww_1j_fid'     : elePtCor_Syst ,
                   'ZH_hww_2j_fid'     : elePtCor_Syst ,
                   'ZH_hww_3j_fid'     : elePtCor_Syst ,
                   'ZH_hww_4j_fid'     : elePtCor_Syst ,
                   'ZH_hww_0j_nonfid'     : elePtCor_Syst ,
                   'ZH_hww_1j_nonfid'     : elePtCor_Syst ,
                   'ZH_hww_2j_nonfid'     : elePtCor_Syst ,
                   'ZH_hww_3j_nonfid'     : elePtCor_Syst ,
                   'ZH_hww_4j_nonfid'     : elePtCor_Syst ,
                   #
#                   'XH_hww_0j_fid'     : elePtCor_Syst ,
#                   'XH_hww_1j_fid'     : elePtCor_Syst ,
#                   'XH_hww_2j_fid'     : elePtCor_Syst ,
#                   'XH_hww_3j_fid'     : elePtCor_Syst ,
#                   'XH_hww_4j_fid'     : elePtCor_Syst ,
#                   'XH_hww_0j_nonfid'     : elePtCor_Syst ,
#                   'XH_hww_1j_nonfid'     : elePtCor_Syst ,
#                   'XH_hww_2j_nonfid'     : elePtCor_Syst ,
#                   'XH_hww_3j_nonfid'     : elePtCor_Syst ,
#                   'XH_hww_4j_nonfid'     : elePtCor_Syst ,
                   #
                   'ggZH_hww'   : elePtCor_Syst ,
                   'bbH_hww'    : elePtCor_Syst ,
                   'ttH_hww'    : elePtCor_Syst ,
                   'H_htt'      : elePtCor_Syst ,
                   'ggH_htt'    : elePtCor_Syst ,
                   'qqH_htt'    : elePtCor_Syst ,
                   'ZH_htt'     : elePtCor_Syst ,
                   'WH_htt'     : elePtCor_Syst ,
                   #
                   'ggH_hww_0j_fid'   : elePtCor_Syst , 
                   'ggH_hww_1j_fid'   : elePtCor_Syst ,
                   'ggH_hww_2j_fid'   : elePtCor_Syst ,
                   'ggH_hww_3j_fid'   : elePtCor_Syst ,
                   'ggH_hww_4j_fid'   : elePtCor_Syst , 
                   'ggH_hww_0j_nonfid': elePtCor_Syst , 
                   'ggH_hww_1j_nonfid': elePtCor_Syst ,
                   'ggH_hww_2j_nonfid': elePtCor_Syst ,
                   'ggH_hww_3j_nonfid': elePtCor_Syst ,
                   'ggH_hww_4j_nonfid': elePtCor_Syst ,
                   #
                   'qqH_hww_0j_fid'   : elePtCor_Syst ,
                   'qqH_hww_1j_fid'   : elePtCor_Syst ,
                   'qqH_hww_2j_fid'   : elePtCor_Syst ,
                   'qqH_hww_3j_fid'   : elePtCor_Syst ,
                   'qqH_hww_4j_fid'   : elePtCor_Syst ,
                   'qqH_hww_0j_nonfid': elePtCor_Syst ,
                   'qqH_hww_1j_nonfid': elePtCor_Syst ,
                   'qqH_hww_2j_nonfid': elePtCor_Syst ,
                   'qqH_hww_3j_nonfid': elePtCor_Syst ,
                   'qqH_hww_4j_nonfid': elePtCor_Syst ,
                   # 
                   'ZH_hww'           : elePtCor_Syst ,
                   #
                   'ggZH_hww'         : elePtCor_Syst ,
                   # 
                   'WH_hww'           : elePtCor_Syst ,
                   #
                   'bbH_hww'          : elePtCor_Syst ,
                   'ttH_hww'          : elePtCor_Syst ,
                   #
                   'ggH_htt'          : elePtCor_Syst ,
                   #
                   'qqH_htt'          : elePtCor_Syst ,
                   # 
                   'ZH_htt'           : elePtCor_Syst ,
                   # 
                   'WH_htt'           : elePtCor_Syst ,
                }
}

eleEtaCor_Syst = [ 'electron_etaW_'+Nlep+'l_Up / electron_etaW_'+Nlep+'l', 'electron_etaW_'+Nlep+'l_Down / electron_etaW_'+Nlep+'l']

nuisances['eleEtaCor']  = {
                'name'  : 'hww_eleEtaCor_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'         : eleEtaCor_Syst ,
                   'ggWW'       : eleEtaCor_Syst ,
                   'WW'         : eleEtaCor_Syst ,
                   'top'        : eleEtaCor_Syst ,
                   'VZ'         : eleEtaCor_Syst ,
                   'WZgS_L'     : eleEtaCor_Syst ,
                   'WZgS_H'     : eleEtaCor_Syst ,
                   'VVV'        : eleEtaCor_Syst ,
                   'Vg'         : eleEtaCor_Syst ,
                   'VgS'        : eleEtaCor_Syst ,
                   'ggH_hww '   : eleEtaCor_Syst ,
                   'qqH_hww '   : eleEtaCor_Syst ,
                   'WH_hww_0j_fid'     : eleEtaCor_Syst ,
                   'WH_hww_1j_fid'     : eleEtaCor_Syst ,
                   'WH_hww_2j_fid'     : eleEtaCor_Syst ,
                   'WH_hww_3j_fid'     : eleEtaCor_Syst ,
                   'WH_hww_4j_fid'     : eleEtaCor_Syst ,
                   'WH_hww_0j_nonfid'     : eleEtaCor_Syst ,
                   'WH_hww_1j_nonfid'     : eleEtaCor_Syst ,
                   'WH_hww_2j_nonfid'     : eleEtaCor_Syst ,
                   'WH_hww_3j_nonfid'     : eleEtaCor_Syst ,
                   'WH_hww_4j_nonfid'     : eleEtaCor_Syst ,
                   'ZH_hww_0j_fid'     : eleEtaCor_Syst ,
                   'ZH_hww_1j_fid'     : eleEtaCor_Syst ,
                   'ZH_hww_2j_fid'     : eleEtaCor_Syst ,
                   'ZH_hww_3j_fid'     : eleEtaCor_Syst ,
                   'ZH_hww_4j_fid'     : eleEtaCor_Syst ,
                   'ZH_hww_0j_nonfid'     : eleEtaCor_Syst ,
                   'ZH_hww_1j_nonfid'     : eleEtaCor_Syst ,
                   'ZH_hww_2j_nonfid'     : eleEtaCor_Syst ,
                   'ZH_hww_3j_nonfid'     : eleEtaCor_Syst ,
                   'ZH_hww_4j_nonfid'     : eleEtaCor_Syst ,
                   #
#                   'XH_hww_0j_fid'     : eleEtaCor_Syst ,
#                   'XH_hww_1j_fid'     : eleEtaCor_Syst ,
#                   'XH_hww_2j_fid'     : eleEtaCor_Syst ,
#                   'XH_hww_3j_fid'     : eleEtaCor_Syst ,
#                   'XH_hww_4j_fid'     : eleEtaCor_Syst ,
#                   'XH_hww_0j_nonfid'     : eleEtaCor_Syst ,
#                   'XH_hww_1j_nonfid'     : eleEtaCor_Syst ,
#                   'XH_hww_2j_nonfid'     : eleEtaCor_Syst ,
#                   'XH_hww_3j_nonfid'     : eleEtaCor_Syst ,
#                   'XH_hww_4j_nonfid'     : eleEtaCor_Syst ,
                   #
                   'ggZH_hww'   : eleEtaCor_Syst ,
                   'bbH_hww'    : eleEtaCor_Syst ,
                   'ttH_hww'    : eleEtaCor_Syst ,
                   'H_htt'      : eleEtaCor_Syst ,
                   'ggH_htt'    : eleEtaCor_Syst ,
                   'qqH_htt'    : eleEtaCor_Syst ,
                   'ZH_htt'     : eleEtaCor_Syst ,
                   'WH_htt'     : eleEtaCor_Syst ,
                   #
                   'ggH_hww_0j_fid'   : eleEtaCor_Syst , 
                   'ggH_hww_1j_fid'   : eleEtaCor_Syst ,
                   'ggH_hww_2j_fid'   : eleEtaCor_Syst ,
                   'ggH_hww_3j_fid'   : eleEtaCor_Syst ,
                   'ggH_hww_4j_fid'   : eleEtaCor_Syst , 
                   'ggH_hww_0j_nonfid': eleEtaCor_Syst , 
                   'ggH_hww_1j_nonfid': eleEtaCor_Syst ,
                   'ggH_hww_2j_nonfid': eleEtaCor_Syst ,
                   'ggH_hww_3j_nonfid': eleEtaCor_Syst ,
                   'ggH_hww_4j_nonfid': eleEtaCor_Syst ,
                   #
                   'qqH_hww_0j_fid'   : eleEtaCor_Syst ,
                   'qqH_hww_1j_fid'   : eleEtaCor_Syst ,
                   'qqH_hww_2j_fid'   : eleEtaCor_Syst ,
                   'qqH_hww_3j_fid'   : eleEtaCor_Syst ,
                   'qqH_hww_4j_fid'   : eleEtaCor_Syst ,
                   'qqH_hww_0j_nonfid': eleEtaCor_Syst ,
                   'qqH_hww_1j_nonfid': eleEtaCor_Syst ,
                   'qqH_hww_2j_nonfid': eleEtaCor_Syst ,
                   'qqH_hww_3j_nonfid': eleEtaCor_Syst ,
                   'qqH_hww_4j_nonfid': eleEtaCor_Syst ,
                   # 
                   'ZH_hww'           : eleEtaCor_Syst , 
                   'ZH_had_hww'       : eleEtaCor_Syst ,
                   'ZH_lep_hww'       : eleEtaCor_Syst ,
                   #
                   'ggZH_hww'         : eleEtaCor_Syst ,
                   'ggZH_lep_hww'     : eleEtaCor_Syst ,
                   # 
                   'WH_hww'           : eleEtaCor_Syst ,
                   #
                   'bbH_hww'          : eleEtaCor_Syst ,
                   'ttH_hww'          : eleEtaCor_Syst ,
                   #
                   'ggH_htt'          : eleEtaCor_Syst ,
                   #
                   'qqH_htt'          : eleEtaCor_Syst ,
                   # 
                   'ZH_htt'           : eleEtaCor_Syst ,
                   # 
                   'WH_htt'           : eleEtaCor_Syst ,
                }
}


##### Muon Efficiency and energy scale

id_syst_mu = [ 'LepSF'+Nlep+'l__mu_'+muWP+'__Up' , 'LepSF'+Nlep+'l__mu_'+muWP+'__Do' ]

nuisances['eff_m']  = {
                'name'  : 'eff_m_2016',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : id_syst_mu ,
                   'VVV'     : id_syst_mu ,
                   'VZ'      : id_syst_mu ,
                   'WZgS_L'  : id_syst_mu ,
                   'WZgS_H'  : id_syst_mu ,
                   'ggWW'    : id_syst_mu ,
                   'WW'      : id_syst_mu ,
                   'top'     : id_syst_mu ,
                   'Vg'      : id_syst_mu ,
                   'VgS'     : id_syst_mu ,
                   'ggH_hww' : id_syst_mu ,
                   'qqH_hww' : id_syst_mu ,
                   'WH_hww_0j_fid'  : id_syst_mu ,
                   'WH_hww_1j_fid'  : id_syst_mu ,
                   'WH_hww_2j_fid'  : id_syst_mu ,
                   'WH_hww_3j_fid'  : id_syst_mu ,
                   'WH_hww_4j_fid'  : id_syst_mu ,
                   'WH_hww_0j_nonfid'  : id_syst_mu ,
                   'WH_hww_1j_nonfid'  : id_syst_mu ,
                   'WH_hww_2j_nonfid'  : id_syst_mu ,
                   'WH_hww_3j_nonfid'  : id_syst_mu ,
                   'WH_hww_4j_nonfid'  : id_syst_mu ,
                   'ZH_hww_0j_fid'  : id_syst_mu ,
                   'ZH_hww_1j_fid'  : id_syst_mu ,
                   'ZH_hww_2j_fid'  : id_syst_mu ,
                   'ZH_hww_3j_fid'  : id_syst_mu ,
                   'ZH_hww_4j_fid'  : id_syst_mu ,
                   'ZH_hww_0j_nonfid'  : id_syst_mu ,
                   'ZH_hww_1j_nonfid'  : id_syst_mu ,
                   'ZH_hww_2j_nonfid'  : id_syst_mu ,
                   'ZH_hww_3j_nonfid'  : id_syst_mu ,
                   'ZH_hww_4j_nonfid'  : id_syst_mu ,
                   #
#                   'XH_hww_0j_fid'  : id_syst_mu ,
#                   'XH_hww_1j_fid'  : id_syst_mu ,
#                   'XH_hww_2j_fid'  : id_syst_mu ,
#                   'XH_hww_3j_fid'  : id_syst_mu ,
#                   'XH_hww_4j_fid'  : id_syst_mu ,
#                   'XH_hww_0j_nonfid'  : id_syst_mu ,
#                   'XH_hww_1j_nonfid'  : id_syst_mu ,
#                   'XH_hww_2j_nonfid'  : id_syst_mu ,
#                   'XH_hww_3j_nonfid'  : id_syst_mu ,
#                   'XH_hww_4j_nonfid'  : id_syst_mu ,
                   #
                   'ggZH_hww': id_syst_mu ,
                   'bbH_hww' : id_syst_mu ,
                   'ttH_hww' : id_syst_mu ,
                   'H_htt'   : id_syst_mu ,
                   'ggH_htt' : id_syst_mu ,
                   'qqH_htt' : id_syst_mu ,
                   'ZH_htt'  : id_syst_mu ,
                   'WH_htt'  : id_syst_mu ,
                   #
                   'ggH_hww_0j_fid'   : id_syst_mu , 
                   'ggH_hww_1j_fid'   : id_syst_mu ,
                   'ggH_hww_2j_fid'   : id_syst_mu ,
                   'ggH_hww_3j_fid'   : id_syst_mu ,
                   'ggH_hww_4j_fid'   : id_syst_mu , 
                   'ggH_hww_0j_nonfid': id_syst_mu , 
                   'ggH_hww_1j_nonfid': id_syst_mu ,
                   'ggH_hww_2j_nonfid': id_syst_mu ,
                   'ggH_hww_3j_nonfid': id_syst_mu ,
                   'ggH_hww_4j_nonfid': id_syst_mu , 
                   #
                   'qqH_hww_0j_fid'   : id_syst_mu ,
                   'qqH_hww_1j_fid'   : id_syst_mu ,
                   'qqH_hww_2j_fid'   : id_syst_mu ,
                   'qqH_hww_3j_fid'   : id_syst_mu ,
                   'qqH_hww_4j_fid'   : id_syst_mu ,
                   'qqH_hww_0j_nonfid': id_syst_mu ,
                   'qqH_hww_1j_nonfid': id_syst_mu ,
                   'qqH_hww_2j_nonfid': id_syst_mu ,
                   'qqH_hww_3j_nonfid': id_syst_mu ,
                   'qqH_hww_4j_nonfid': id_syst_mu ,
                   # 
                   'ZH_hww'           : id_syst_mu ,
                   #
                   'ggZH_hww'         : id_syst_mu ,
                   # 
                   'WH_hww'           : id_syst_mu ,
                   #
                   'bbH_hww'          : id_syst_mu ,
                   'ttH_hww'          : id_syst_mu ,
                   #
                   'ggH_htt'          : id_syst_mu ,
                   #
                   'qqH_htt'          : id_syst_mu ,
                   # 
                   'ZH_htt'           : id_syst_mu ,
                   # 
                   'WH_htt'           : id_syst_mu ,
                },
}

nuisances['muonpt']  = {
                'name'  : 'scale_m_2016',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['1', '1'],
                   'ggWW'    : ['1', '1'],
                   'WW'      : ['1', '1'],
                   'top'     : ['1', '1'],
                   'VZ'      : ['1', '1'],
                   'WZgS_L'  : ['1', '1'],
                   'WZgS_H'  : ['1', '1'],
                   'VVV'     : ['1', '1'],
                   'Vg'      : ['1', '1'],
                   'VgS'     : ['1', '1'],
                   'ggH_hww ': ['1', '1'],
                   'qqH_hww ': ['1', '1'],
                   'WH_hww_0j_fid'  : ['1', '1'],
                   'WH_hww_1j_fid'  : ['1', '1'],
                   'WH_hww_2j_fid'  : ['1', '1'],
                   'WH_hww_3j_fid'  : ['1', '1'],
                   'WH_hww_4j_fid'  : ['1', '1'],
                   'WH_hww_0j_nonfid'  : ['1', '1'],
                   'WH_hww_1j_nonfid'  : ['1', '1'],
                   'WH_hww_2j_nonfid'  : ['1', '1'],
                   'WH_hww_3j_nonfid'  : ['1', '1'],
                   'WH_hww_4j_nonfid'  : ['1', '1'],
                   'ZH_hww_0j_fid'  : ['1', '1'],
                   'ZH_hww_1j_fid'  : ['1', '1'],
                   'ZH_hww_2j_fid'  : ['1', '1'],
                   'ZH_hww_3j_fid'  : ['1', '1'],
                   'ZH_hww_4j_fid'  : ['1', '1'],
                   'ZH_hww_0j_nonfid'  : ['1', '1'],
                   'ZH_hww_1j_nonfid'  : ['1', '1'],
                   'ZH_hww_2j_nonfid'  : ['1', '1'],
                   'ZH_hww_3j_nonfid'  : ['1', '1'],
                   'ZH_hww_4j_nonfid'  : ['1', '1'],
                   #
#                   'XH_hww_0j_fid'  : ['1', '1'],
#                   'XH_hww_1j_fid'  : ['1', '1'],
#                   'XH_hww_2j_fid'  : ['1', '1'],
#                   'XH_hww_3j_fid'  : ['1', '1'],
#                   'XH_hww_4j_fid'  : ['1', '1'],
#                   'XH_hww_0j_nonfid'  : ['1', '1'],
#                   'XH_hww_1j_nonfid'  : ['1', '1'],
#                   'XH_hww_2j_nonfid'  : ['1', '1'],
#                   'XH_hww_3j_nonfid'  : ['1', '1'],
#                   'XH_hww_4j_nonfid'  : ['1', '1'],
                   #
                   'ggZH_hww': ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'ttH_hww' : ['1', '1'],
                   'H_htt'   : ['1', '1'],
                   'ggH_htt' : ['1', '1'] ,
                   'qqH_htt' : ['1', '1'] ,
                   'ZH_htt'  : ['1', '1'] ,
                   'WH_htt'  : ['1', '1'] ,
                   #
                   'ggH_hww_0j_fid'   : ['1', '1'] , 
                   'ggH_hww_1j_fid'   : ['1', '1'] ,
                   'ggH_hww_2j_fid'   : ['1', '1'] ,
                   'ggH_hww_3j_fid'   : ['1', '1'] ,
                   'ggH_hww_4j_fid'   : ['1', '1'] , 
                   'ggH_hww_0j_nonfid': ['1', '1'] , 
                   'ggH_hww_1j_nonfid': ['1', '1'] ,
                   'ggH_hww_2j_nonfid': ['1', '1'] ,
                   'ggH_hww_3j_nonfid': ['1', '1'] ,
                   'ggH_hww_4j_nonfid': ['1', '1'] , 
                   #
                   'qqH_hww_0j_fid'   : ['1', '1'] ,
                   'qqH_hww_1j_fid'   : ['1', '1'] ,
                   'qqH_hww_2j_fid'   : ['1', '1'] ,
                   'qqH_hww_3j_fid'   : ['1', '1'] ,
                   'qqH_hww_4j_fid'   : ['1', '1'] ,
                   'qqH_hww_0j_nonfid': ['1', '1'] ,
                   'qqH_hww_1j_nonfid': ['1', '1'] ,
                   'qqH_hww_2j_nonfid': ['1', '1'] ,
                   'qqH_hww_3j_nonfid': ['1', '1'] ,
                   'qqH_hww_4j_nonfid': ['1', '1'] ,
                   # 
                   'ZH_hww'           : ['1', '1'],
                   #
                   'ggZH_hww'         : ['1', '1'],
                   # 
                   'WH_hww'           : ['1', '1'],
                   #
                   'bbH_hww'          : ['1', '1'],
                   'ttH_hww'          : ['1', '1'],
                   #
                   'ggH_htt'          : ['1', '1'],
                   #
                   'qqH_htt'          : ['1', '1'],
                   # 
                   'ZH_htt'           : ['1', '1'],
                   # 
                   'WH_htt'           : ['1', '1'],
                },
                'folderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__LepMupTup'+skim,
                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__LepMupTdo'+skim,
}


##### Jet energy scale

nuisances['jes']  = {
                'name'  : 'scale_j_2016',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['1', '1'],
                   'ggWW'    : ['1', '1'],
                   'WW'      : ['1', '1'],
                   'top'     : ['1', '1'],
                   'VZ'      : ['1', '1'],
                   'WZgS_L'  : ['1', '1'],
                   'WZgS_H'  : ['1', '1'],
                   'VVV'     : ['1', '1'],
                   'Vg'      : ['1', '1'],
                   'VgS'     : ['1', '1'],
                   'ggH_hww ': ['1', '1'],
                   'qqH_hww ': ['1', '1'],
                   'WH_hww_0j_fid'  : ['1', '1'],
                   'WH_hww_1j_fid'  : ['1', '1'],
                   'WH_hww_2j_fid'  : ['1', '1'],
                   'WH_hww_3j_fid'  : ['1', '1'],
                   'WH_hww_4j_fid'  : ['1', '1'],
                   'WH_hww_0j_nonfid'  : ['1', '1'],
                   'WH_hww_1j_nonfid'  : ['1', '1'],
                   'WH_hww_2j_nonfid'  : ['1', '1'],
                   'WH_hww_3j_nonfid'  : ['1', '1'],
                   'WH_hww_4j_nonfid'  : ['1', '1'],
                   'ZH_hww_0j_fid'  : ['1', '1'],
                   'ZH_hww_1j_fid'  : ['1', '1'],
                   'ZH_hww_2j_fid'  : ['1', '1'],
                   'ZH_hww_3j_fid'  : ['1', '1'],
                   'ZH_hww_4j_fid'  : ['1', '1'],
                   'ZH_hww_0j_nonfid'  : ['1', '1'],
                   'ZH_hww_1j_nonfid'  : ['1', '1'],
                   'ZH_hww_2j_nonfid'  : ['1', '1'],
                   'ZH_hww_3j_nonfid'  : ['1', '1'],
                   'ZH_hww_4j_nonfid'  : ['1', '1'],
                   #
#                   'XH_hww_0j_fid'  : ['1', '1'],
#                   'XH_hww_1j_fid'  : ['1', '1'],
#                   'XH_hww_2j_fid'  : ['1', '1'],
#                   'XH_hww_3j_fid'  : ['1', '1'],
#                   'XH_hww_4j_fid'  : ['1', '1'],
#                   'XH_hww_0j_nonfid'  : ['1', '1'],
#                   'XH_hww_1j_nonfid'  : ['1', '1'],
#                   'XH_hww_2j_nonfid'  : ['1', '1'],
#                   'XH_hww_3j_nonfid'  : ['1', '1'],
#                   'XH_hww_4j_nonfid'  : ['1', '1'],
                   #
                   'ggZH_hww': ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'ttH_hww' : ['1', '1'],
                   'H_htt'   : ['1', '1'],
                   'ggH_htt' : ['1', '1'] ,
                   'qqH_htt' : ['1', '1'] ,
                   'ZH_htt'  : ['1', '1'] ,
                   'WH_htt'  : ['1', '1'] ,
                   #
                   'ggH_hww_0j_fid'   : ['1', '1'] , 
                   'ggH_hww_1j_fid'   : ['1', '1'] ,
                   'ggH_hww_2j_fid'   : ['1', '1'] ,
                   'ggH_hww_3j_fid'   : ['1', '1'] ,
                   'ggH_hww_4j_fid'   : ['1', '1'] , 
                   'ggH_hww_0j_nonfid': ['1', '1'] , 
                   'ggH_hww_1j_nonfid': ['1', '1'] ,
                   'ggH_hww_2j_nonfid': ['1', '1'] ,
                   'ggH_hww_3j_nonfid': ['1', '1'] ,
                   'ggH_hww_4j_nonfid': ['1', '1'] ,
                   #
                   'qqH_hww_0j_fid'   : ['1', '1'] ,
                   'qqH_hww_1j_fid'   : ['1', '1'] ,
                   'qqH_hww_2j_fid'   : ['1', '1'] ,
                   'qqH_hww_3j_fid'   : ['1', '1'] ,
                   'qqH_hww_4j_fid'   : ['1', '1'] ,
                   'qqH_hww_0j_nonfid': ['1', '1'] ,
                   'qqH_hww_1j_nonfid': ['1', '1'] ,
                   'qqH_hww_2j_nonfid': ['1', '1'] ,
                   'qqH_hww_3j_nonfid': ['1', '1'] ,
                   'qqH_hww_4j_nonfid': ['1', '1'] ,
                   # 
                   'ZH_hww'           : ['1', '1'],
                   #
                   'ggZH_hww'         : ['1', '1'],
                   # 
                   'WH_hww'           : ['1', '1'],
                   #
                   'bbH_hww'          : ['1', '1'],
                   'ttH_hww'          : ['1', '1'],
                   #
                   'ggH_htt'          : ['1', '1'],
                   #
                   'qqH_htt'          : ['1', '1'],
                   # 
                   'ZH_htt'           : ['1', '1'],
                   # 
                   'WH_htt'           : ['1', '1'],
                },
                'folderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__JESup'+skim,
                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__JESdo'+skim,
}

##### MET energy scale

nuisances['met']  = {
                'name'  : 'scale_met_2016',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['1', '1'],
                   'ggWW'    : ['1', '1'],
                   'WW'      : ['1', '1'],
                   'top'     : ['1', '1'],
                   'VZ'      : ['1', '1'],
                   'WZgS_L'  : ['1', '1'],
                   'WZgS_H'  : ['1', '1'],
                   'VVV'     : ['1', '1'],
                   'Vg'      : ['1', '1'],
                   'VgS'     : ['1', '1'],
                   'ggH_hww ': ['1', '1'],
                   'qqH_hww ': ['1', '1'],
                   'WH_hww_0j_fid'  : ['1', '1'],
                   'WH_hww_1j_fid'  : ['1', '1'],
                   'WH_hww_2j_fid'  : ['1', '1'],
                   'WH_hww_3j_fid'  : ['1', '1'],
                   'WH_hww_4j_fid'  : ['1', '1'],
                   'WH_hww_0j_nonfid'  : ['1', '1'],
                   'WH_hww_1j_nonfid'  : ['1', '1'],
                   'WH_hww_2j_nonfid'  : ['1', '1'],
                   'WH_hww_3j_nonfid'  : ['1', '1'],
                   'WH_hww_4j_nonfid'  : ['1', '1'],
                   'ZH_hww_0j_fid'  : ['1', '1'],
                   'ZH_hww_1j_fid'  : ['1', '1'],
                   'ZH_hww_2j_fid'  : ['1', '1'],
                   'ZH_hww_3j_fid'  : ['1', '1'],
                   'ZH_hww_4j_fid'  : ['1', '1'],
                   'ZH_hww_0j_nonfid'  : ['1', '1'],
                   'ZH_hww_1j_nonfid'  : ['1', '1'],
                   'ZH_hww_2j_nonfid'  : ['1', '1'],
                   'ZH_hww_3j_nonfid'  : ['1', '1'],
                   'ZH_hww_4j_nonfid'  : ['1', '1'],
                   #
#                   'XH_hww_0j_fid'  : ['1', '1'],
#                   'XH_hww_1j_fid'  : ['1', '1'],
#                   'XH_hww_2j_fid'  : ['1', '1'],
#                   'XH_hww_3j_fid'  : ['1', '1'],
#                   'XH_hww_4j_fid'  : ['1', '1'],
#                   'XH_hww_0j_nonfid'  : ['1', '1'],
#                   'XH_hww_1j_nonfid'  : ['1', '1'],
#                   'XH_hww_2j_nonfid'  : ['1', '1'],
#                   'XH_hww_3j_nonfid'  : ['1', '1'],
#                   'XH_hww_4j_nonfid'  : ['1', '1'],
                   #
                   'ggZH_hww': ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'ttH_hww' : ['1', '1'],
                   'H_htt'   : ['1', '1'],
                   'ggH_htt' : ['1', '1'] ,
                   'qqH_htt' : ['1', '1'] ,
                   'ZH_htt'  : ['1', '1'] ,
                   'WH_htt'  : ['1', '1'] ,
                   #
                   'ggH_hww_0j_fid'   : ['1', '1'] , 
                   'ggH_hww_1j_fid'   : ['1', '1'] ,
                   'ggH_hww_2j_fid'   : ['1', '1'] ,
                   'ggH_hww_3j_fid'   : ['1', '1'] ,
                   'ggH_hww_4j_fid'   : ['1', '1'] , 
                   'ggH_hww_0j_nonfid': ['1', '1'] , 
                   'ggH_hww_1j_nonfid': ['1', '1'] ,
                   'ggH_hww_2j_nonfid': ['1', '1'] ,
                   'ggH_hww_3j_nonfid': ['1', '1'] ,
                   'ggH_hww_4j_nonfid': ['1', '1'] , 
                   #
                   'qqH_hww_0j_fid'   : ['1', '1'] ,
                   'qqH_hww_1j_fid'   : ['1', '1'] ,
                   'qqH_hww_2j_fid'   : ['1', '1'] ,
                   'qqH_hww_3j_fid'   : ['1', '1'] ,
                   'qqH_hww_4j_fid'   : ['1', '1'] ,
                   'qqH_hww_0j_nonfid': ['1', '1'] ,
                   'qqH_hww_1j_nonfid': ['1', '1'] ,
                   'qqH_hww_2j_nonfid': ['1', '1'] ,
                   'qqH_hww_3j_nonfid': ['1', '1'] ,
                   'qqH_hww_4j_nonfid': ['1', '1'] ,
                   # 
                   'ZH_hww'           : ['1', '1'],
                   #
                   'ggZH_hww'         : ['1', '1'],
                   # 
                   'WH_hww'           : ['1', '1'],
                   #
                   'bbH_hww'          : ['1', '1'],
                   'ttH_hww'          : ['1', '1'],
                   #
                   'ggH_htt'          : ['1', '1'],
                   #
                   'qqH_htt'          : ['1', '1'],
                   # 
                   'ZH_htt'           : ['1', '1'],
                   # 
                   'WH_htt'           : ['1', '1'],
                },
                'folderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__METup'+skim,
                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__METdo'+skim,
}

#
# PS and UE
#

nuisances['PS']  = {
                'name'  : 'PS_2016',
                'skipCMS' : 1,
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                  'WW'      : ['0.92657', '1.'], #
                  'ggH_hww_0j_fid' 		: ['0.98554', '1.'], # These numbers are used to normalize the PS variation to the same integral as the nominal after the wwSel skim
                  'ggH_hww_1j_fid' 		: ['0.98554', '1.'],
                  'ggH_hww_2j_fid' 		: ['0.98554', '1.'],
                  #'ggH_hww_0j_nonfid' : ['0.98554', '1.'],
                  #'ggH_hww_1j_nonfid' : ['0.98554', '1.'],
                  #'ggH_hww_2j_nonfid' : ['0.98554', '1.'],
                  #'ggH_fwd_hww' : ['0.98554', '1.'],
                  #'qqH_hww_0j_fid' 		: ['0.92511', '1.'], #
                  #'qqH_hww_1j_fid' 		: ['0.92511', '1.'], #
                  #'qqH_hww_2j_fid' 		: ['0.92511', '1.'], #
                  #'qqH_hww_0j_nonfid' : ['0.92511', '1.'], #
                  #'qqH_hww_1j_nonfid' : ['0.92511', '1.'], #
                  #'qqH_hww_2j_nonfid' : ['0.92511', '1.'], #
                  #'qqH_fwd_hww' : ['0.92511', '1.'],

                },
                'folderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__PS'+skim,
                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC'+skim,
                'AsLnN'      : '1',
                }

nuisances['UE']  = {
                'name'  : 'UE_2016', 
                'skipCMS' : 1,
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                  'WW'      : ['1.0226', '0.9897'],
                  'ggH_hww_0j_fid' 		:     ['1.0739', '1.0211'],
                  'ggH_hww_1j_fid' 		:     ['1.0739', '1.0211'],
                  'ggH_hww_2j_fid' 		:     ['1.0739', '1.0211'],
                  #'ggH_hww_0j_nonfid' :     ['1.0739', '1.0211'],
                  #'ggH_hww_1j_nonfid' :     ['1.0739', '1.0211'],
                  #'ggH_hww_2j_nonfid' :     ['1.0739', '1.0211'],
                  #'ggH_fwd_hww' : ['1.0739', '1.0211'],  
                  #'qqH_hww_0j_fid' 		:     ['1.0560', '0.9992'], #
                  #'qqH_hww_1j_fid' 	 	:     ['1.0560', '0.9992'], #
                  #'qqH_hww_2j_fid' 	 	:     ['1.0560', '0.9992'], #
                  #'qqH_hww_0j_nonfid' 	:     ['1.0560', '0.9992'], #
                  #'qqH_hww_1j_nonfid' 	:     ['1.0560', '0.9992'], #
                  #'qqH_hww_2j_nonfid' 	:     ['1.0560', '0.9992'], #
                  #'qqH_fwd_hww' : ['1.0560', '0.9992'], #
                },
                'folderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__UEup'+skim,
                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__UEdo'+skim,
                'AsLnN'      : '1',
                }

'''
## Shape nuisance due to QCD scale variations for DY
nuisances['DYQCDscale']  = {
                'name'  : 'QCDscale_V',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['std_vector_LHE_weight[8]/std_vector_LHE_weight[0]', 'std_vector_LHE_weight[4]/std_vector_LHE_weight[0]'],
                }
}

'''
#
#
# Theory uncertainty for ggH
#
#
#   THU_ggH_Mu, THU_ggH_Res, THU_ggH_Mig01, THU_ggH_Mig12, THU_ggH_VBF2j, THU_ggH_VBF3j, THU_ggH_PT60, THU_ggH_PT120, THU_ggH_qmtop
#
#   see https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsWG/SignalModelingTools
#
#


nuisances['ggH_mu']  = {
                'name'  : 'THU_ggH_Mu',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'ggH_hww_0j_fid'       : ['0.956862481999*ggH_mu', '1.04721061556*(1+(1.-ggH_mu))'],
                   'ggH_hww_1j_fid'       : ['0.956862481999*ggH_mu', '1.04721061556*(1+(1.-ggH_mu))'],
                   'ggH_hww_2j_fid'       : ['0.956862481999*ggH_mu', '1.04721061556*(1+(1.-ggH_mu))'],
                   'ggH_hww_3j_fid'       : ['0.956862481999*ggH_mu', '1.04721061556*(1+(1.-ggH_mu))'],
                   'ggH_hww_4j_fid'       : ['0.956862481999*ggH_mu', '1.04721061556*(1+(1.-ggH_mu))'],
                   'ggH_hww_0j_nonfid'    : ['0.956862481999*ggH_mu', '1.04721061556*(1+(1.-ggH_mu))'],
                   'ggH_hww_1j_nonfid'    : ['0.956862481999*ggH_mu', '1.04721061556*(1+(1.-ggH_mu))'],
                   'ggH_hww_2j_nonfid'    : ['0.956862481999*ggH_mu', '1.04721061556*(1+(1.-ggH_mu))'],
                   'ggH_hww_3j_nonfid'    : ['0.956862481999*ggH_mu', '1.04721061556*(1+(1.-ggH_mu))'],
                   'ggH_hww_4j_nonfid'    : ['0.956862481999*ggH_mu', '1.04721061556*(1+(1.-ggH_mu))'],
                   'ggH_htt'       : ['ggH_mu', '1+(1.-ggH_mu)'],
                   },
                }


nuisances['ggH_res']  = {
                'name'  : 'THU_ggH_Res',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'ggH_hww_0j_fid'       : ['0.976053022102*ggH_res', '1.02515158689*(1+(1.-ggH_res))'],
                   'ggH_hww_1j_fid'       : ['0.976053022102*ggH_res', '1.02515158689*(1+(1.-ggH_res))'],
                   'ggH_hww_2j_fid'       : ['0.976053022102*ggH_res', '1.02515158689*(1+(1.-ggH_res))'],
                   'ggH_hww_3j_fid'       : ['0.976053022102*ggH_res', '1.02515158689*(1+(1.-ggH_res))'],
                   'ggH_hww_4j_fid'       : ['0.976053022102*ggH_res', '1.02515158689*(1+(1.-ggH_res))'],
                   'ggH_hww_0j_nonfid'    : ['0.976053022102*ggH_res', '1.02515158689*(1+(1.-ggH_res))'],
                   'ggH_hww_1j_nonfid'    : ['0.976053022102*ggH_res', '1.02515158689*(1+(1.-ggH_res))'],
                   'ggH_hww_2j_nonfid'    : ['0.976053022102*ggH_res', '1.02515158689*(1+(1.-ggH_res))'],
                   'ggH_hww_3j_nonfid'    : ['0.976053022102*ggH_res', '1.02515158689*(1+(1.-ggH_res))'],
                   'ggH_hww_4j_nonfid'    : ['0.976053022102*ggH_res', '1.02515158689*(1+(1.-ggH_res))'],
                   'ggH_htt'       : ['ggH_res', '1+(1.-ggH_res)'],
                   },
                }

nuisances['ggH_mig01']  = {
                'name'  : 'THU_ggH_Mig01',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'ggH_hww_0j_fid'       : ['0.978541312796*ggH_mig01', '1.02242093486*(1+(1.-ggH_mig01))'],
                   'ggH_hww_1j_fid'       : ['0.978541312796*ggH_mig01', '1.02242093486*(1+(1.-ggH_mig01))'],
                   'ggH_hww_2j_fid'       : ['0.978541312796*ggH_mig01', '1.02242093486*(1+(1.-ggH_mig01))'],
                   'ggH_hww_3j_fid'       : ['0.978541312796*ggH_mig01', '1.02242093486*(1+(1.-ggH_mig01))'],
                   'ggH_hww_4j_fid'       : ['0.978541312796*ggH_mig01', '1.02242093486*(1+(1.-ggH_mig01))'],
                   'ggH_hww_0j_nonfid'    : ['0.978541312796*ggH_mig01', '1.02242093486*(1+(1.-ggH_mig01))'],
                   'ggH_hww_1j_nonfid'    : ['0.978541312796*ggH_mig01', '1.02242093486*(1+(1.-ggH_mig01))'],
                   'ggH_hww_2j_nonfid'    : ['0.978541312796*ggH_mig01', '1.02242093486*(1+(1.-ggH_mig01))'],
                   'ggH_hww_3j_nonfid'    : ['0.978541312796*ggH_mig01', '1.02242093486*(1+(1.-ggH_mig01))'],
                   'ggH_hww_4j_nonfid'    : ['0.978541312796*ggH_mig01', '1.02242093486*(1+(1.-ggH_mig01))'],
                   'ggH_htt'       : ['ggH_mig01', '1+(1.-ggH_mig01)'],
                   },
                }

nuisances['ggH_mig12']  = {
                'name'  : 'THU_ggH_Mig12',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'ggH_hww_0j_fid'       : ['1.03354649125*ggH_mig12', '0.968562729019*(1+(1.-ggH_mig12))'],
                   'ggH_hww_1j_fid'       : ['1.03354649125*ggH_mig12', '0.968562729019*(1+(1.-ggH_mig12))'],
                   'ggH_hww_2j_fid'       : ['1.03354649125*ggH_mig12', '0.968562729019*(1+(1.-ggH_mig12))'],
                   'ggH_hww_3j_fid'       : ['1.03354649125*ggH_mig12', '0.968562729019*(1+(1.-ggH_mig12))'],
                   'ggH_hww_4j_fid'       : ['1.03354649125*ggH_mig12', '0.968562729019*(1+(1.-ggH_mig12))'],
                   'ggH_hww_0j_nonfid'    : ['1.03354649125*ggH_mig12', '0.968562729019*(1+(1.-ggH_mig12))'],
                   'ggH_hww_1j_nonfid'    : ['1.03354649125*ggH_mig12', '0.968562729019*(1+(1.-ggH_mig12))'],
                   'ggH_hww_2j_nonfid'    : ['1.03354649125*ggH_mig12', '0.968562729019*(1+(1.-ggH_mig12))'],
                   'ggH_hww_3j_nonfid'    : ['1.03354649125*ggH_mig12', '0.968562729019*(1+(1.-ggH_mig12))'],
                   'ggH_hww_4j_nonfid'    : ['1.03354649125*ggH_mig12', '0.968562729019*(1+(1.-ggH_mig12))'],
                   'ggH_htt'       : ['ggH_mig12', '1+(1.-ggH_mig12)'],
                   },
                }

nuisances['ggH_pT60']  = {
                'name'  : 'THU_ggH_PT60',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'ggH_hww_0j_fid'       : ['0.986873455747*ggH_pT60', '1.01348044764*(1+(1.-ggH_pT60))'],
                   'ggH_hww_1j_fid'       : ['0.986873455747*ggH_pT60', '1.01348044764*(1+(1.-ggH_pT60))'],
                   'ggH_hww_2j_fid'       : ['0.986873455747*ggH_pT60', '1.01348044764*(1+(1.-ggH_pT60))'],
                   'ggH_hww_3j_fid'       : ['0.986873455747*ggH_pT60', '1.01348044764*(1+(1.-ggH_pT60))'],
                   'ggH_hww_4j_fid'       : ['0.986873455747*ggH_pT60', '1.01348044764*(1+(1.-ggH_pT60))'],
                   'ggH_hww_0j_nonfid'    : ['0.986873455747*ggH_pT60', '1.01348044764*(1+(1.-ggH_pT60))'],
                   'ggH_hww_1j_nonfid'    : ['0.986873455747*ggH_pT60', '1.01348044764*(1+(1.-ggH_pT60))'],
                   'ggH_hww_2j_nonfid'    : ['0.986873455747*ggH_pT60', '1.01348044764*(1+(1.-ggH_pT60))'],
                   'ggH_hww_3j_nonfid'    : ['0.986873455747*ggH_pT60', '1.01348044764*(1+(1.-ggH_pT60))'],
                   'ggH_hww_4j_nonfid'    : ['0.986873455747*ggH_pT60', '1.01348044764*(1+(1.-ggH_pT60))'],
                   'ggH_htt'       : ['ggH_pT60', '1+(1.-ggH_pT60)'],
                   },
                }

nuisances['ggH_pT120']  = {
                'name'  : 'THU_ggH_PT120',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'ggH_hww_0j_fid'       : ['0.991114238973*ggH_pT120', '1.00904653166*(1+(1.-ggH_pT120))'],
                   'ggH_hww_1j_fid'       : ['0.991114238973*ggH_pT120', '1.00904653166*(1+(1.-ggH_pT120))'],
                   'ggH_hww_2j_fid'       : ['0.991114238973*ggH_pT120', '1.00904653166*(1+(1.-ggH_pT120))'],
                   'ggH_hww_3j_fid'       : ['0.991114238973*ggH_pT120', '1.00904653166*(1+(1.-ggH_pT120))'],
                   'ggH_hww_4j_fid'       : ['0.991114238973*ggH_pT120', '1.00904653166*(1+(1.-ggH_pT120))'],
                   'ggH_hww_0j_nonfid'    : ['0.991114238973*ggH_pT120', '1.00904653166*(1+(1.-ggH_pT120))'],
                   'ggH_hww_1j_nonfid'    : ['0.991114238973*ggH_pT120', '1.00904653166*(1+(1.-ggH_pT120))'],
                   'ggH_hww_2j_nonfid'    : ['0.991114238973*ggH_pT120', '1.00904653166*(1+(1.-ggH_pT120))'],
                   'ggH_hww_3j_nonfid'    : ['0.991114238973*ggH_pT120', '1.00904653166*(1+(1.-ggH_pT120))'],
                   'ggH_hww_4j_nonfid'    : ['0.991114238973*ggH_pT120', '1.00904653166*(1+(1.-ggH_pT120))'],
                   'ggH_htt'       : ['ggH_pT120', '1+(1.-ggH_pT120)'],
                   },
                }

nuisances['ggH_VBF2j']  = {
                'name'  : 'THU_ggH_VBF2j',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'ggH_hww_0j_fid'       : ['0.99565225214*ggH_VBF2j', '1.00438588531*(1+(1.-ggH_VBF2j))'],
                   'ggH_hww_1j_fid'       : ['0.99565225214*ggH_VBF2j', '1.00438588531*(1+(1.-ggH_VBF2j))'],
                   'ggH_hww_2j_fid'       : ['0.99565225214*ggH_VBF2j', '1.00438588531*(1+(1.-ggH_VBF2j))'],
                   'ggH_hww_3j_fid'       : ['0.99565225214*ggH_VBF2j', '1.00438588531*(1+(1.-ggH_VBF2j))'],
                   'ggH_hww_4j_fid'       : ['0.99565225214*ggH_VBF2j', '1.00438588531*(1+(1.-ggH_VBF2j))'],
                   'ggH_hww_0j_nonfid'    : ['0.99565225214*ggH_VBF2j', '1.00438588531*(1+(1.-ggH_VBF2j))'],
                   'ggH_hww_1j_nonfid'    : ['0.99565225214*ggH_VBF2j', '1.00438588531*(1+(1.-ggH_VBF2j))'],
                   'ggH_hww_2j_nonfid'    : ['0.99565225214*ggH_VBF2j', '1.00438588531*(1+(1.-ggH_VBF2j))'],
                   'ggH_hww_3j_nonfid'    : ['0.99565225214*ggH_VBF2j', '1.00438588531*(1+(1.-ggH_VBF2j))'],
                   'ggH_hww_4j_nonfid'    : ['0.99565225214*ggH_VBF2j', '1.00438588531*(1+(1.-ggH_VBF2j))'],
                   'ggH_htt'       : ['ggH_VBF2j', '1+(1.-ggH_VBF2j)'],
                   },
                }

nuisances['ggH_VBF3j']  = {
                'name'  : 'THU_ggH_VBF3j',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'ggH_hww_0j_fid'       : ['0.999899080749*ggH_VBF3j', '1.00010093962*(1+(1.-ggH_VBF3j))'],
                   'ggH_hww_1j_fid'       : ['0.999899080749*ggH_VBF3j', '1.00010093962*(1+(1.-ggH_VBF3j))'],
                   'ggH_hww_2j_fid'       : ['0.999899080749*ggH_VBF3j', '1.00010093962*(1+(1.-ggH_VBF3j))'],
                   'ggH_hww_3j_fid'       : ['0.999899080749*ggH_VBF3j', '1.00010093962*(1+(1.-ggH_VBF3j))'],
                   'ggH_hww_4j_fid'       : ['0.999899080749*ggH_VBF3j', '1.00010093962*(1+(1.-ggH_VBF3j))'],
                   'ggH_hww_0j_nonfid'    : ['0.999899080749*ggH_VBF3j', '1.00010093962*(1+(1.-ggH_VBF3j))'],
                   'ggH_hww_1j_nonfid'    : ['0.999899080749*ggH_VBF3j', '1.00010093962*(1+(1.-ggH_VBF3j))'],
                   'ggH_hww_2j_nonfid'    : ['0.999899080749*ggH_VBF3j', '1.00010093962*(1+(1.-ggH_VBF3j))'],
                   'ggH_hww_3j_nonfid'    : ['0.999899080749*ggH_VBF3j', '1.00010093962*(1+(1.-ggH_VBF3j))'],
                   'ggH_hww_4j_nonfid'    : ['0.999899080749*ggH_VBF3j', '1.00010093962*(1+(1.-ggH_VBF3j))'],
                   'ggH_htt'       : ['ggH_VBF3j', '1+(1.-ggH_VBF3j)'],
                   },
                }

nuisances['ggH_qmtop']  = {
                'name'  : 'THU_ggH_qmtop',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'ggH_hww_0j_fid'       : ['0.995393164223*ggH_qmtop', '1.00464967637*(1+(1.-ggH_qmtop))'],
                   'ggH_hww_1j_fid'       : ['0.995393164223*ggH_qmtop', '1.00464967637*(1+(1.-ggH_qmtop))'],
                   'ggH_hww_2j_fid'       : ['0.995393164223*ggH_qmtop', '1.00464967637*(1+(1.-ggH_qmtop))'],
                   'ggH_hww_3j_fid'       : ['0.995393164223*ggH_qmtop', '1.00464967637*(1+(1.-ggH_qmtop))'],
                   'ggH_hww_4j_fid'       : ['0.995393164223*ggH_qmtop', '1.00464967637*(1+(1.-ggH_qmtop))'],
                   'ggH_hww_0j_nonfid'    : ['0.995393164223*ggH_qmtop', '1.00464967637*(1+(1.-ggH_qmtop))'],
                   'ggH_hww_1j_nonfid'    : ['0.995393164223*ggH_qmtop', '1.00464967637*(1+(1.-ggH_qmtop))'],
                   'ggH_hww_2j_nonfid'    : ['0.995393164223*ggH_qmtop', '1.00464967637*(1+(1.-ggH_qmtop))'],
                   'ggH_hww_3j_nonfid'    : ['0.995393164223*ggH_qmtop', '1.00464967637*(1+(1.-ggH_qmtop))'],
                   'ggH_hww_4j_nonfid'    : ['0.995393164223*ggH_qmtop', '1.00464967637*(1+(1.-ggH_qmtop))'],
                   'ggH_htt'       : ['ggH_qmtop', '1+(1.-ggH_qmtop)'],
                   },
                }

nuisances['QCDscale_CRSR_accept_dytt']  = {
               'name'  : 'CMS_hww_QCDscale_CRSR_accept_dytt', 
               'type'  : 'lnN',
               'samples'  : {
                   'DY' : '1.02',
                   },
               'cuts'  : [
                 'hww2l2v_13TeV_dytt_of0j',
                 'hww2l2v_13TeV_dytt_of1j',
                 'hww2l2v_13TeV_dytt_of2j',
                 'hww2l2v_13TeV_dytt_of3j',
                 'hww2l2v_13TeV_dytt_of4j',
                ]               
              }

nuisances['QCDscale_CRSR_accept_top']  = {
               'name'  : 'CMS_hww_QCDscale_CRSR_accept_top', 
               'type'  : 'lnN',
               'samples'  : {
                   'top' : '1.01',
                   },
               'cuts'  : [
                 'hww2l2v_13TeV_top_of0j',
                 'hww2l2v_13TeV_top_of1j',
                 'hww2l2v_13TeV_top_of2j',
                 'hww2l2v_13TeV_top_of3j',
                 'hww2l2v_13TeV_top_of4j',
                ]               
              }


nuisances['QCDscale_VZ']  = {
               'name'  : 'QCDscale_VZ', 
               'samples'  : {
                   'VZ' : '1.03',
                   },
               'type'  : 'lnN'
              }



#### QCD scale uncertainties for Higgs signals other than ggH

from LatinoAnalysis.Tools.HiggsXSection  import *
HiggsXS = HiggsXSection()

nuisances['QCDscale_ggH']  = {
               'name'  : 'QCDscale_ggH', 
               'samples'  : {
                   'H_htt'   : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH','125.0','scale','sm'),
                   },
               'type'  : 'lnN',
              }


nuisances['QCDscale_qqH']  = {
               'name'  : 'QCDscale_qqH', 
               'samples'  : {
                   'qqH_hww_0j_fid'     : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','scale','sm'),
                   'qqH_hww_1j_fid'     : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','scale','sm'),
                   'qqH_hww_2j_fid'     : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','scale','sm'),
                   'qqH_hww_3j_fid'     : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','scale','sm'),
                   'qqH_hww_4j_fid'     : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','scale','sm'),
                   'qqH_hww_0j_nonfid'  : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','scale','sm'),
                   'qqH_hww_1j_nonfid'  : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','scale','sm'),
                   'qqH_hww_2j_nonfid'  : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','scale','sm'),
                   'qqH_hww_3j_nonfid'  : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','scale','sm'),
                   'qqH_hww_4j_nonfid'  : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','scale','sm'),
                   'qqH_htt'     : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','scale','sm'),
                   },
               'type'  : 'lnN',
              }

nuisances['QCDscale_VH']  = {
               'name'  : 'QCDscale_VH', 
               'samples'  : {
                   'WH_hww_0j_fid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   'WH_hww_1j_fid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   'WH_hww_2j_fid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   'WH_hww_3j_fid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   'WH_hww_4j_fid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   'WH_hww_0j_nonfid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   'WH_hww_1j_nonfid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   'WH_hww_2j_nonfid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   'WH_hww_3j_nonfid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   'WH_hww_4j_nonfid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   #
                   'WH_htt'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   # 
                   'ZH_hww_0j_fid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   'ZH_hww_1j_fid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   'ZH_hww_2j_fid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   'ZH_hww_3j_fid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   'ZH_hww_4j_fid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   'ZH_hww_0j_nonfid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   'ZH_hww_1j_nonfid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   'ZH_hww_2j_nonfid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   'ZH_hww_3j_nonfid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   'ZH_hww_4j_nonfid'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   # 
                   'ZH_htt'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ZH','125.0','scale','sm'),
                   },
               'type'  : 'lnN',
              }

nuisances['QCDscale_ggZH']  = {
               'name'  : 'QCDscale_ggZH', 
               'samples'  : {
                   'ggZH_hww': HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggZH','125.0','scale','sm'),
                   },
               'type'  : 'lnN',
              }

nuisances['QCDscale_bbH']  = {
               'name'  : 'QCDscale_bbH',
               'samples'  : {
                   'bbH_hww': HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','bbH','125.0','scale','sm'),
                   },
               'type'  : 'lnN',
              }

nuisances['QCDscale_ttH']  = {
               'name'  : 'QCDscale_ttH',
               'samples'  : {
                   'ttH_hww': HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ttH','125.0','scale','sm'),
                   },
               'type'  : 'lnN',
              }

nuisances['QCDscale_qqbar_ACCEPT']  = {
               'name'  : 'QCDscale_qqbar_ACCEPT', 
               'type'  : 'lnN',
               'samples'  : {
                   'VZ'      : '1.029',
                   #
                   'qqH_hww_0j_fid'     : '1.007',
                   'qqH_hww_1j_fid'     : '1.007',
                   'qqH_hww_2j_fid'     : '1.007',
                   'qqH_hww_3j_fid'     : '1.007',
                   'qqH_hww_4j_fid'     : '1.007',
                   'qqH_hww_0j_nonfid'  : '1.007',
                   'qqH_hww_1j_nonfid'  : '1.007',
                   'qqH_hww_2j_nonfid'  : '1.007',
                   'qqH_hww_3j_nonfid'  : '1.007',
                   'qqH_hww_4j_nonfid'  : '1.007',
                   # 
                   'qqH_htt'     : '1.007',
                   # 
                   'WH_hww_0j_fid'          : '1.05',
                   'WH_hww_1j_fid'          : '1.05',
                   'WH_hww_2j_fid'          : '1.05',
                   'WH_hww_3j_fid'          : '1.05',
                   'WH_hww_4j_fid'          : '1.05',
                   'WH_hww_0j_nonfid'          : '1.05',
                   'WH_hww_1j_nonfid'          : '1.05',
                   'WH_hww_2j_nonfid'          : '1.05',
                   'WH_hww_3j_nonfid'          : '1.05',
                   'WH_hww_4j_nonfid'          : '1.05',
                   #
                   'XH_hww_0j_fid'          : '1.05',
                   'XH_hww_1j_fid'          : '1.05',
                   'XH_hww_2j_fid'          : '1.05',
                   'XH_hww_3j_fid'          : '1.05',
                   'XH_hww_4j_fid'          : '1.05',
                   'XH_hww_0j_nonfid'          : '1.05',
                   'XH_hww_1j_nonfid'          : '1.05',
                   'XH_hww_2j_nonfid'          : '1.05',
                   'XH_hww_3j_nonfid'          : '1.05',
                   'XH_hww_4j_nonfid'          : '1.05',
                   #
                   'WH_htt'          : '1.05',
                   # 
                   'ZH_hww_0j_fid'          : '1.05',
                   'ZH_hww_1j_fid'          : '1.05',
                   'ZH_hww_2j_fid'          : '1.05',
                   'ZH_hww_3j_fid'          : '1.05',
                   'ZH_hww_4j_fid'          : '1.05',
                   'ZH_hww_0j_nonfid'          : '1.05',
                   'ZH_hww_1j_nonfid'          : '1.05',
                   'ZH_hww_2j_nonfid'          : '1.05',
                   'ZH_hww_3j_nonfid'          : '1.05',
                   'ZH_hww_4j_nonfid'          : '1.05',
                   #
                   'ZH_htt'          : '1.04',
                   },
              }


nuisances['QCDscale_gg_ACCEPT']  = {
               'name'  : 'QCDscale_gg_ACCEPT', 
               'samples'  : {
                   'ggWW'    : '1.027',
                   'ggWW'    : '1.027',
                   #
                   'ggH_hww_0j_fid'     : '1.027',
                   'ggH_hww_1j_fid'     : '1.027',
                   'ggH_hww_2j_fid'     : '1.027',
                   'ggH_hww_3j_fid'     : '1.027',
                   'ggH_hww_4j_fid'     : '1.027',
                   'ggH_hww_0j_nonfid'  : '1.027',
                   'ggH_hww_1j_nonfid'  : '1.027',
                   'ggH_hww_2j_nonfid'  : '1.027',
                   'ggH_hww_3j_nonfid'  : '1.027',
                   'ggH_hww_4j_nonfid'  : '1.027',
                   # 
                   'ggH_htt'     : '1.027',
                   #
                   'ggZH_hww'         : '1.027',
                   },
               'type'  : 'lnN',
              }

###### pdf uncertainty

nuisances['pdf_Higgs_gg']  = {
               'name'  : 'pdf_Higgs_gg', 
               'samples'  : {
                   'ggH_hww_0j_fid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH' ,'125.0','pdf','sm'),
                   'ggH_hww_1j_fid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH' ,'125.0','pdf','sm'),
                   'ggH_hww_2j_fid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH' ,'125.0','pdf','sm'),
                   'ggH_hww_3j_fid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH' ,'125.0','pdf','sm'),
                   'ggH_hww_4j_fid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH' ,'125.0','pdf','sm'),
                   'ggH_hww_0j_nonfid'       : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH' ,'125.0','pdf','sm'),
                   'ggH_hww_1j_nonfid'       : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH' ,'125.0','pdf','sm'),
                   'ggH_hww_2j_nonfid'       : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH' ,'125.0','pdf','sm'),
                   'ggH_hww_3j_nonfid'       : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH' ,'125.0','pdf','sm'),
                   'ggH_hww_4j_nonfid'       : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH' ,'125.0','pdf','sm'),
                   #
                   'ggH_htt'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH' ,'125.0','pdf','sm'),
                   #
                   'ggZH_hww'         : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggZH','125.0','pdf','sm'),                   
                   #
                   'bbH_hww'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','bbH' ,'125.0','pdf','sm'),
                   },
               'type'  : 'lnN',
              }

nuisances['pdf_Higgs_ttH']  = {
               'name'  : 'pdf_Higgs_ttH',
               'samples'  : {
                   'ttH_hww'     : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ttH' ,'125.0','pdf','sm'),
                   },
               'type'  : 'lnN',
              }

nuisances['pdf_Higgs_qqbar']  = {
               'name'  : 'pdf_Higgs_qqbar', 
               'type'  : 'lnN',
               'samples'  : {
                   'qqH_hww_0j_fid'     : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','pdf','sm'),
                   'qqH_hww_1j_fid'     : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','pdf','sm'),
                   'qqH_hww_2j_fid'     : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','pdf','sm'),
                   'qqH_hww_3j_fid'     : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','pdf','sm'),
                   'qqH_hww_4j_fid'     : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','pdf','sm'),
                   'qqH_hww_0j_nonfid'  : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','pdf','sm'),
                   'qqH_hww_1j_nonfid'  : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','pdf','sm'),
                   'qqH_hww_2j_nonfid'  : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','pdf','sm'),
                   'qqH_hww_3j_nonfid'  : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','pdf','sm'),
                   'qqH_hww_4j_nonfid'  : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','pdf','sm'),
                   'qqH_htt'     : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','pdf','sm'),
                   #
                   'WH_hww_0j_fid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   'WH_hww_1j_fid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   'WH_hww_2j_fid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   'WH_hww_3j_fid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   'WH_hww_4j_fid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   'WH_hww_0j_nonfid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   'WH_hww_1j_nonfid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   'WH_hww_2j_nonfid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   'WH_hww_3j_nonfid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   'WH_hww_4j_nonfid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   #
                   'WH_htt'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),     
                   # 
                   'ZH_hww_0j_fid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   'ZH_hww_1j_fid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   'ZH_hww_2j_fid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   'ZH_hww_3j_fid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   'ZH_hww_4j_fid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   'ZH_hww_0j_nonfid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   'ZH_hww_1j_nonfid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   'ZH_hww_2j_nonfid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   'ZH_hww_3j_nonfid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   'ZH_hww_4j_nonfid'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   #
                   'ZH_htt'          : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ZH' ,'125.0','pdf','sm'),
                   },
              }

nuisances['pdf_qqbar']  = {
               'name'  : 'pdf_qqbar',
               'type'  : 'lnN',
               'samples'  : {
                   'VZ'      : '1.04',  # PDF: 0.0064 / 0.1427 = 0.0448493
                   },
              }


nuisances['pdf_Higgs_gg_ACCEPT']  = {
               'name'  : 'pdf_Higgs_gg_ACCEPT', 
               'samples'  : {
                   'ggH_hww_0j_fid'     : '1.005',
                   'ggH_hww_1j_fid'     : '1.005',
                   'ggH_hww_2j_fid'     : '1.005',
                   'ggH_hww_3j_fid'     : '1.005',
                   'ggH_hww_4j_fid'     : '1.005',
                   'ggH_hww_0j_nonfid'  : '1.005',
                   'ggH_hww_1j_nonfid'  : '1.005',
                   'ggH_hww_2j_nonfid'  : '1.005',
                   'ggH_hww_3j_nonfid'  : '1.005',
                   'ggH_hww_4j_nonfid'  : '1.005',
                   # 
                   'ggH_htt'     : '1.005',
                   # 
                   'ggZH_hww'         : '1.005',
                   },
               'type'  : 'lnN',
              }

nuisances['pdf_gg_ACCEPT']  = {
               'name'  : 'pdf_gg_ACCEPT',
               'samples'  : {
                   'ggWW'    : '1.005',
                   },
               'type'  : 'lnN',
              }

nuisances['pdf_Higgs_qqbar_ACCEPT']  = {
               'name'  : 'pdf_Higgs_qqbar_ACCEPT',
               'type'  : 'lnN',
               'samples'  : {
                   #
                   'qqH_hww_0j_fid'     : '1.011',
                   'qqH_hww_1j_fid'     : '1.011',
                   'qqH_hww_2j_fid'     : '1.011',
                   'qqH_hww_3j_fid'     : '1.011',
                   'qqH_hww_4j_fid'     : '1.011',
                   'qqH_hww_0j_nonfid'  : '1.011',
                   'qqH_hww_1j_nonfid'  : '1.011',
                   'qqH_hww_2j_nonfid'  : '1.011',
                   'qqH_hww_3j_nonfid'  : '1.011',
                   'qqH_hww_4j_nonfid'  : '1.011',
                   #
                   'qqH_htt' : '1.011',
                   # 
                   'WH_hww_0j_fid'          : '1.007',
                   'WH_hww_1j_fid'          : '1.007',
                   'WH_hww_2j_fid'          : '1.007',
                   'WH_hww_3j_fid'          : '1.007',
                   'WH_hww_4j_fid'          : '1.007',
                   'WH_hww_0j_nonfid'          : '1.007',
                   'WH_hww_1j_nonfid'          : '1.007',
                   'WH_hww_2j_nonfid'          : '1.007',
                   'WH_hww_3j_nonfid'          : '1.007',
                   'WH_hww_4j_nonfid'          : '1.007',
                   # 
                   'WH_htt'          : '1.007',
                   # 
                   'ZH_hww_0j_fid'          : '1.007',
                   'ZH_hww_1j_fid'          : '1.007',
                   'ZH_hww_2j_fid'          : '1.007',
                   'ZH_hww_3j_fid'          : '1.007',
                   'ZH_hww_4j_fid'          : '1.007',
                   'ZH_hww_0j_nonfid'          : '1.007',
                   'ZH_hww_1j_nonfid'          : '1.007',
                   'ZH_hww_2j_nonfid'          : '1.007',
                   'ZH_hww_3j_nonfid'          : '1.007',
                   'ZH_hww_4j_nonfid'          : '1.007',
                   #
                   'XH_hww_0j_fid'          : '1.007',
                   'XH_hww_1j_fid'          : '1.007',
                   'XH_hww_2j_fid'          : '1.007',
                   'XH_hww_3j_fid'          : '1.007',
                   'XH_hww_4j_fid'          : '1.007',
                   'XH_hww_0j_nonfid'          : '1.007',
                   'XH_hww_1j_nonfid'          : '1.007',
                   'XH_hww_2j_nonfid'          : '1.007',
                   'XH_hww_3j_nonfid'          : '1.007',
                   'XH_hww_4j_nonfid'          : '1.007',
                   #
                   'ZH_htt'          : '1.012',
                   },
              }

nuisances['pdf_qqbar_ACCEPT']  = {
               'name'  : 'pdf_qqbar_ACCEPT',
               'type'  : 'lnN',
               'samples'  : {
                   #
                   'VZ'      : '1.005',
                   },
              }

# ggww and interference

nuisances['QCDscale_ggWW']  = {
               'name'  : 'QCDscale_ggWW',
               'type'  : 'lnN',
               'samples'  : {
                   'ggWW' : '1.15',
                   },
              }

#  - WW shaping
nuisances['WWresum0j']  = {
                'name'  : 'WWresum0j',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
                   },
                'cuts'  : [
                 'hww2l2v_13TeV_of0j',
                 'hww2l2v_13TeV_top_of0j',
                 'hww2l2v_13TeV_dytt_of0j',
#                 
                 'hww2l2v_13TeV_me_0j',
                 'hww2l2v_13TeV_em_0j',
#
                 'hww2l2v_13TeV_me_mp_0j',
                 'hww2l2v_13TeV_me_pm_0j',
                 'hww2l2v_13TeV_em_mp_0j',
                 'hww2l2v_13TeV_em_pm_0j',
#                
		 						 'hww2l2v_13TeV_em_pm_0j_pt2ge20',
                 'hww2l2v_13TeV_em_mp_0j_pt2ge20',
                 'hww2l2v_13TeV_me_pm_0j_pt2ge20',
                 'hww2l2v_13TeV_me_mp_0j_pt2ge20',
#
                 'hww2l2v_13TeV_em_pm_0j_pt2lt20',
                 'hww2l2v_13TeV_em_mp_0j_pt2lt20',
                 'hww2l2v_13TeV_me_pm_0j_pt2lt20',
                 'hww2l2v_13TeV_me_mp_0j_pt2lt20',
#
                ]               
                
                }


nuisances['WWresum1j']  = {
                'name'  : 'WWresum1j',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
                   },
               'cuts'  : [
                 'hww2l2v_13TeV_of1j',
                 'hww2l2v_13TeV_top_of1j',
                 'hww2l2v_13TeV_dytt_of1j',
#                 
                 'hww2l2v_13TeV_me_1j',
                 'hww2l2v_13TeV_em_1j',
#
                 'hww2l2v_13TeV_me_mp_1j',
                 'hww2l2v_13TeV_me_pm_1j',
                 'hww2l2v_13TeV_em_mp_1j',
                 'hww2l2v_13TeV_em_pm_1j',
#               
                 'hww2l2v_13TeV_em_pm_1j_pt2ge20',
                 'hww2l2v_13TeV_em_mp_1j_pt2ge20',
                 'hww2l2v_13TeV_me_pm_1j_pt2ge20',
                 'hww2l2v_13TeV_me_mp_1j_pt2ge20',
#
                 'hww2l2v_13TeV_em_pm_1j_pt2lt20',
                 'hww2l2v_13TeV_em_mp_1j_pt2lt20',
                 'hww2l2v_13TeV_me_pm_1j_pt2lt20',
                 'hww2l2v_13TeV_me_mp_1j_pt2lt20',
#
                ]               
                }

nuisances['WWqscale0j']  = {
                'name'  : 'WWqscale0j',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
                   },
               'cuts'  : [
                 'hww2l2v_13TeV_of0j',
                 'hww2l2v_13TeV_top_of0j',
                 'hww2l2v_13TeV_dytt_of0j',
#                 
                 'hww2l2v_13TeV_me_0j',
                 'hww2l2v_13TeV_em_0j',
#
                 'hww2l2v_13TeV_me_mp_0j',
                 'hww2l2v_13TeV_me_pm_0j',
                 'hww2l2v_13TeV_em_mp_0j',
                 'hww2l2v_13TeV_em_pm_0j',
#               
                 'hww2l2v_13TeV_em_pm_0j_pt2ge20',
                 'hww2l2v_13TeV_em_mp_0j_pt2ge20',
                 'hww2l2v_13TeV_me_pm_0j_pt2ge20',
                 'hww2l2v_13TeV_me_mp_0j_pt2ge20',
#                
                 'hww2l2v_13TeV_em_pm_0j_pt2lt20',
                 'hww2l2v_13TeV_em_mp_0j_pt2lt20',
                 'hww2l2v_13TeV_me_pm_0j_pt2lt20',
                 'hww2l2v_13TeV_me_mp_0j_pt2lt20',
#  
                ] 
                }


nuisances['WWqscale1j']  = {
                'name'  : 'WWqscale1j',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
                   },
               'cuts'  : [
                 'hww2l2v_13TeV_of1j',
                 'hww2l2v_13TeV_top_of1j',
                 'hww2l2v_13TeV_dytt_of1j',
#                 
                 'hww2l2v_13TeV_me_1j',
                 'hww2l2v_13TeV_em_1j',
#
                 'hww2l2v_13TeV_me_mp_1j',
                 'hww2l2v_13TeV_me_pm_1j',
                 'hww2l2v_13TeV_em_mp_1j',
                 'hww2l2v_13TeV_em_pm_1j',
#
                 'hww2l2v_13TeV_em_pm_1j_pt2ge20',
                 'hww2l2v_13TeV_em_mp_1j_pt2ge20',
                 'hww2l2v_13TeV_me_pm_1j_pt2ge20',
                 'hww2l2v_13TeV_me_mp_1j_pt2ge20',
#
                 'hww2l2v_13TeV_em_pm_1j_pt2lt20',
                 'hww2l2v_13TeV_em_mp_1j_pt2lt20',
                 'hww2l2v_13TeV_me_pm_1j_pt2lt20',
                 'hww2l2v_13TeV_me_mp_1j_pt2lt20',
#                 
                ] 
                }
                
nuisances['WWresum2j']  = {
                'name'  : 'WWresum2j',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
                },
               'cuts'  : [
                 'hww2l2v_13TeV_of2j',
                 'hww2l2v_13TeV_top_of2j',
                 'hww2l2v_13TeV_dytt_of2j',
                ]
                }
                
nuisances['WWresum3j']  = {
                'name'  : 'WWresum3j',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
                },
               'cuts'  : [
                 'hww2l2v_13TeV_of3j',
                 'hww2l2v_13TeV_top_of3j',
                 'hww2l2v_13TeV_dytt_of3j',
                ]
                }
                
nuisances['WWresum4j']  = {
                'name'  : 'WWresum4j',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
                },
               'cuts'  : [
                 'hww2l2v_13TeV_of4j',
                 'hww2l2v_13TeV_top_of4j',
                 'hww2l2v_13TeV_dytt_of4j',
                ]
                }

nuisances['WWqscale2j']  = {
                'name'  : 'WWqscale2j',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
                },
                'cuts'  : [
                 'hww2l2v_13TeV_of2j',
                 'hww2l2v_13TeV_top_of2j',
                 'hww2l2v_13TeV_dytt_of2j',
                ]
                }
                
nuisances['WWqscale3j']  = {
                'name'  : 'WWqscale3j',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
                },
                'cuts'  : [
                 'hww2l2v_13TeV_of3j',
                 'hww2l2v_13TeV_top_of3j',
                 'hww2l2v_13TeV_dytt_of3j',
                ]
                }
                
nuisances['WWqscale4j']  = {
                'name'  : 'WWqscale4j',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
                },
                'cuts'  : [
                 'hww2l2v_13TeV_of4j',
                 'hww2l2v_13TeV_top_of4j',
                 'hww2l2v_13TeV_dytt_of4j',
                ]
                }

nuisances['WgStarScale']  = {
               'name'  : 'CMS_hww_WgStarScale', 
               'type'  : 'lnN',
               'samples'  : {
                   'WgS'    : '1.25',  # 0.5 / 2.0   --> k_factor = 2.0 +/- 0.5
                   'VgS'    : '1.25',  # 0.5 / 2.0   --> k_factor = 2.0 +/- 0.5
                   'WZgS_L' : '1.25',  
                   },
                }
 
nuisances['WZScale'] = {
               'name'  : 'CMS_hww_WZScale',
               'type'  : 'lnN',
               'samples'  : {
                   'WZgS_H' : '1.16', 
                   },
                }

nuisances['DYttnorm0j']  = {
               'name'  : 'CMS_hww_DYttnorm0j', 
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of0j',
                 'hww2l2v_13TeV_top_of0j',
                 'hww2l2v_13TeV_dytt_of0j',
#                 
                 'hww2l2v_13TeV_me_0j',
                 'hww2l2v_13TeV_em_0j',
#
                 'hww2l2v_13TeV_me_mp_0j',
                 'hww2l2v_13TeV_me_pm_0j',
                 'hww2l2v_13TeV_em_mp_0j',
                 'hww2l2v_13TeV_em_pm_0j',
#
                 'hww2l2v_13TeV_em_pm_0j_pt2ge20',
                 'hww2l2v_13TeV_em_mp_0j_pt2ge20',
                 'hww2l2v_13TeV_me_pm_0j_pt2ge20',
                 'hww2l2v_13TeV_me_mp_0j_pt2ge20',
#                
                 'hww2l2v_13TeV_em_pm_0j_pt2lt20',
                 'hww2l2v_13TeV_em_mp_0j_pt2lt20',
                 'hww2l2v_13TeV_me_pm_0j_pt2lt20',
                 'hww2l2v_13TeV_me_mp_0j_pt2lt20',
#
                ]
              }

nuisances['DYttnorm1j']  = {
               'name'  : 'CMS_hww_DYttnorm1j', 
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of1j',
                 'hww2l2v_13TeV_top_of1j',
                 'hww2l2v_13TeV_dytt_of1j',
#                 
                 'hww2l2v_13TeV_me_1j',
                 'hww2l2v_13TeV_em_1j',
#
                 'hww2l2v_13TeV_me_mp_1j',
                 'hww2l2v_13TeV_me_pm_1j',
                 'hww2l2v_13TeV_em_mp_1j',
                 'hww2l2v_13TeV_em_pm_1j',
#
                 'hww2l2v_13TeV_em_pm_1j_pt2ge20',
                 'hww2l2v_13TeV_em_mp_1j_pt2ge20',
                 'hww2l2v_13TeV_me_pm_1j_pt2ge20',
                 'hww2l2v_13TeV_me_mp_1j_pt2ge20',
#
                 'hww2l2v_13TeV_em_pm_1j_pt2lt20',
                 'hww2l2v_13TeV_em_mp_1j_pt2lt20',
                 'hww2l2v_13TeV_me_pm_1j_pt2lt20',
                 'hww2l2v_13TeV_me_mp_1j_pt2lt20',
#                 
                ]
              }
              
nuisances['DYttnorm2j']  = {
               'name'  : 'CMS_hww_DYttnorm2j', 
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of2j',
                 'hww2l2v_13TeV_top_of2j',
                 'hww2l2v_13TeV_dytt_of2j',
                ]
              }
              
nuisances['DYttnorm3j']  = {
               'name'  : 'CMS_hww_DYttnorm3j', 
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of3j',
                 'hww2l2v_13TeV_top_of3j',
                 'hww2l2v_13TeV_dytt_of3j',
                ]
              }
              
nuisances['DYttnorm4j']  = {
               'name'  : 'CMS_hww_DYttnorm4j', 
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of4j',
                 'hww2l2v_13TeV_top_of4j',
                 'hww2l2v_13TeV_dytt_of4j',
                ]
              }

nuisances['WWnorm0j']  = {
               'name'  : 'CMS_hww_WWnorm0j', 
               'samples'  : {
                   'WW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of0j',
                 'hww2l2v_13TeV_top_of0j',
                 'hww2l2v_13TeV_dytt_of0j',              
#                 
                 'hww2l2v_13TeV_me_0j',
                 'hww2l2v_13TeV_em_0j',
#
                 'hww2l2v_13TeV_me_mp_0j',
                 'hww2l2v_13TeV_me_pm_0j',
                 'hww2l2v_13TeV_em_mp_0j',
                 'hww2l2v_13TeV_em_pm_0j',
#                
                 'hww2l2v_13TeV_em_pm_0j_pt2ge20',
                 'hww2l2v_13TeV_em_mp_0j_pt2ge20',
                 'hww2l2v_13TeV_me_pm_0j_pt2ge20',
                 'hww2l2v_13TeV_me_mp_0j_pt2ge20',
#                
                 'hww2l2v_13TeV_em_pm_0j_pt2lt20',
                 'hww2l2v_13TeV_em_mp_0j_pt2lt20',
                 'hww2l2v_13TeV_me_pm_0j_pt2lt20',
                 'hww2l2v_13TeV_me_mp_0j_pt2lt20',
#
                ]
              }

nuisances['WWnorm1j']  = {
               'name'  : 'CMS_hww_WWnorm1j', 
               'samples'  : {
                   'WW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of1j',
                 'hww2l2v_13TeV_top_of1j',
                 'hww2l2v_13TeV_dytt_of1j',              
#                 
                 'hww2l2v_13TeV_me_1j',
                 'hww2l2v_13TeV_em_1j',
#
                 'hww2l2v_13TeV_me_mp_1j',
                 'hww2l2v_13TeV_me_pm_1j',
                 'hww2l2v_13TeV_em_mp_1j',
                 'hww2l2v_13TeV_em_pm_1j',
#               
                 'hww2l2v_13TeV_em_pm_1j_pt2ge20',
                 'hww2l2v_13TeV_em_mp_1j_pt2ge20',
                 'hww2l2v_13TeV_me_pm_1j_pt2ge20',
                 'hww2l2v_13TeV_me_mp_1j_pt2ge20',
#
                 'hww2l2v_13TeV_em_pm_1j_pt2lt20',
                 'hww2l2v_13TeV_em_mp_1j_pt2lt20',
                 'hww2l2v_13TeV_me_pm_1j_pt2lt20',
                 'hww2l2v_13TeV_me_mp_1j_pt2lt20',
#  
                ]
              }
              
nuisances['WWnorm2j']  = {
               'name'  : 'CMS_hww_WWnorm2j', 
               'samples'  : {
                   'WW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of2j',
                 'hww2l2v_13TeV_top_of2j',
                 'hww2l2v_13TeV_dytt_of2j',              
                ]
              }
              
nuisances['WWnorm3j']  = {
               'name'  : 'CMS_hww_WWnorm3j', 
               'samples'  : {
                   'WW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of3j',
                 'hww2l2v_13TeV_top_of3j',
                 'hww2l2v_13TeV_dytt_of3j',              
                ]
              }
              
nuisances['WWnorm4j']  = {
               'name'  : 'CMS_hww_WWnorm4j', 
               'samples'  : {
                   'WW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of4j',
                 'hww2l2v_13TeV_top_of4j',
                 'hww2l2v_13TeV_dytt_of4j',              
                ]
              }


nuisances['Topnorm0j']  = {
               'name'  : 'CMS_hww_Topnorm0j', 
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of0j',
                 'hww2l2v_13TeV_top_of0j',
                 'hww2l2v_13TeV_dytt_of0j',              
#                 
                 'hww2l2v_13TeV_me_0j',
                 'hww2l2v_13TeV_em_0j',
#
                 'hww2l2v_13TeV_me_mp_0j',
                 'hww2l2v_13TeV_me_pm_0j',
                 'hww2l2v_13TeV_em_mp_0j',
                 'hww2l2v_13TeV_em_pm_0j',
#
                 'hww2l2v_13TeV_em_pm_0j_pt2ge20',
                 'hww2l2v_13TeV_em_mp_0j_pt2ge20',
                 'hww2l2v_13TeV_me_pm_0j_pt2ge20',
                 'hww2l2v_13TeV_me_mp_0j_pt2ge20',
#                
                 'hww2l2v_13TeV_em_pm_0j_pt2lt20',
                 'hww2l2v_13TeV_em_mp_0j_pt2lt20',
                 'hww2l2v_13TeV_me_pm_0j_pt2lt20',
                 'hww2l2v_13TeV_me_mp_0j_pt2lt20',
#                
                ]
              }

nuisances['Topnorm1j']  = {
               'name'  : 'CMS_hww_Topnorm1j', 
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of1j',
                 'hww2l2v_13TeV_top_of1j',
                 'hww2l2v_13TeV_dytt_of1j',              
#                 
                 'hww2l2v_13TeV_me_1j',
                 'hww2l2v_13TeV_em_1j',
#
                 'hww2l2v_13TeV_me_mp_1j',
                 'hww2l2v_13TeV_me_pm_1j',
                 'hww2l2v_13TeV_em_mp_1j',
                 'hww2l2v_13TeV_em_pm_1j',
#   
                 'hww2l2v_13TeV_em_pm_1j_pt2ge20',
                 'hww2l2v_13TeV_em_mp_1j_pt2ge20',
                 'hww2l2v_13TeV_me_pm_1j_pt2ge20',
                 'hww2l2v_13TeV_me_mp_1j_pt2ge20',
#
                 'hww2l2v_13TeV_em_pm_1j_pt2lt20',
                 'hww2l2v_13TeV_em_mp_1j_pt2lt20',
                 'hww2l2v_13TeV_me_pm_1j_pt2lt20',
                 'hww2l2v_13TeV_me_mp_1j_pt2lt20',
#              
                ]
              }
              
nuisances['Topnorm2j']  = {
               'name'  : 'CMS_hww_Topnorm2j', 
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of2j',
                 'hww2l2v_13TeV_top_of2j',
                 'hww2l2v_13TeV_dytt_of2j',              
                ]
              }
              
nuisances['Topnorm3j']  = {
               'name'  : 'CMS_hww_Topnorm3j', 
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of3j',
                 'hww2l2v_13TeV_top_of3j',
                 'hww2l2v_13TeV_dytt_of3j',              
                ]
              }
              
nuisances['Topnorm4j']  = {
               'name'  : 'CMS_hww_Topnorm4j', 
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of4j',
                 'hww2l2v_13TeV_top_of4j',
                 'hww2l2v_13TeV_dytt_of4j',              
                ]
              }


nuisances['singleTopToTTbar']  = {
                'name'  : 'singleTopToTTbar',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : { 
                   'top'     : ['((dataset==15 || dataset==16) * 1.0816 + (dataset==17 || dataset==18 || dataset==19))',
                                '((dataset==15 || dataset==16) * 0.9184 + (dataset==17 || dataset==18 || dataset==19))'],
                }
                # tt = 17/18/19 depending on the sample/generator
                # tW = 15/16
           }

## Top pT reweighting uncertainty

nuisances['TopPtRew']  = {
                'name'  : 'TopPtRew',   # Theory uncertainty
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples' : {
                     'top'  : ["1.","((1./"+Top_pTrw+" - 1)*(dataset==19) + 1)"]
                }
         }


## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat']  = {
              'type'  : 'auto',
              'maxPoiss'  : '10',
              'includeSignal'  : '1',
              #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
              #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
              'samples' : {}
             }

#### Use the following if you want to apply the MC stat nuisances accoriding to the standard approach
#nuisances['stat']  = {
#                # apply to the following samples: name of samples here must match keys in samples.py
#               'samples'  : { 
#                   'ttbar': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'singletop': {
#                         'typeStat' : 'bbb',
#                         },
#                    
#                   'top': {
#                         'typeStat' : 'bbb',
#                         },
#                    
#                   'DY': {
#                         'typeStat' : 'bbb',
#                         'keepNormalization' : '1'  # default = 0 -> 0=don't keep normalization
#                         },
#                    
#                   'ggWW': {
#                         'typeStat' : 'bbb',
#                         },
#                    
#                   'ggWW_Int': {
#                         'typeStat' : 'bbb',
#                         },
#                    
#                   'WW': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'VZ': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'WZ': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'VVV': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'H_hww': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'ggH_hww_0j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'ggH_hww_1j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'ggH_hww_2j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'ggH_hww_3j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'ggH_hww_4j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'ggH_hww_0j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'ggH_hww_1j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'ggH_hww_2j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'ggH_hww_3j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'ggH_hww_4j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'qqH_hww_0j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'qqH_hww_1j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'qqH_hww_2j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'qqH_hww_3j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'qqH_hww_4j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'qqH_hww_0j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'qqH_hww_1j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'qqH_hww_2j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'qqH_hww_3j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'qqH_hww_4j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'ZH_hww_0j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'ZH_hww_1j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'ZH_hww_2j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'ZH_hww_3j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'ZH_hww_4j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'ZH_hww_0j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'ZH_hww_1j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'ZH_hww_2j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'ZH_hww_3j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'ZH_hww_4j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         }, 
#                         
#                   'WH_hww_0j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'WH_hww_1j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'WH_hww_2j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'WH_hww_3j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'WH_hww_4j_fid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'WH_hww_0j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'WH_hww_1j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'WH_hww_2j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'WH_hww_3j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         },
#                         
#                   'WH_hww_4j_nonfid': {
#                         'typeStat' : 'bbb',
#                         'zeroMCError' : '1',
#                         }, 
#
#                   'qqH_hww': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'WH_hww': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'ZH_hww': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'H_htt': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'ggH_htt': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'qqH_htt': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'WH_htt': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'ZH_htt': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'ggZH_hww': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'bbH_hww': {
#                         'typeStat' : 'bbb',
#                         },
#                   
#                   'Fake': {
#                         'typeStat' : 'bbb',
#                         },
#                   
#                   'Vg': {  
#                         'typeStat' : 'bbb',
#                         },
#
#                   'VgS':{  
#                         'typeStat' : 'bbb',
#                         },
#                 },
#               'type'  : 'shape'
#              }

