# nuisances


# name of samples here must match keys in samples.py    
#


nuisances['lumi2016']  = {
               'name'  : 'lumi_13TeV_2016', 
               'samples'  : {
                   'chargeMisId'  : '1.025',
                   'Vg'   : '1.025',
#                   'WZ'   : '1.058',
                   'ZZ'   : '1.025',
                   'VVV'  : '1.025',
                   'DPS'   : '1.025',
                   'WpWpJJ'    : '1.025',
                   'WpWpJJ_QCD'    : '1.025',
                   },
               'type'  : 'lnN',
              }



# lumi_13TeV_norm lnN 1.023
# lumi_13TeV_2015 lnN 1.015
# lumi_13TeV_2016 lnN 1.058


#nuisances['WZ_norm']  = {
               #'name'  : 'WZ_norm', 
               #'samples'  : {
                   #'WZ'   : '1.3',
               #'type'  : 'lnN',
              #}
#}

nuisances['charge_flip']  = {
               'name'  : 'charge_flip', 
               'samples'  : {
                   'chargeMisId'   : '1.07',
                   },
               'type'  : 'lnN',
              }


# theory uncertainties

#nuisances['QCDscale']  = {
    #'name'  : 'QCDscale', 
    #'type'  : 'lnN', 
    #'samples'  : { 
        #'chargeMisId'  : '1.10',
        #'WZ'   : '1.10',
        #'ZZ'   : '1.10',
        #'VVV'  : '1.10',
        #'DPS'   : '1.10',
         #'Vg'    : '1.10' ,
         #'WpWpJJ': '1.10' ,
         #'WpWpJJ_QCD': '1.10' ,
    #}, 
#} 



#nuisances['QCDscale_gg_accept']  = { 
    #'name'  : 'QCDscale_gg_accept', 
    #'type'  : 'lnN', 
    #'samples'  : { 
         #'DY': '0.976/1.012' ,
         #'WpWpJJ': '0.994/0.981' ,
    #}, 
 #} 


#nuisances['QCDscale_qqbar_accept']  = { 
    #'name'  : 'QCDscale_qqbar_accept', 
    #'type'  : 'lnN', 
    #'samples'  : { 
         #'lep_TT': '0.974/1.005' ,
         #'Vg': '0.949/1.008' ,
    #}, 
 #} 



# pdf uncertainty

#nuisances['pdf']  = {
    #'name'  : 'pdf',
    #'type'  : 'lnN',
    #'samples'  : {
        #'chargeMisId'  : '1.01',
        #'WZ'   : '1.01',
        #'ZZ'   : '1.01',
        #'VVV'  : '1.01',
        #'DPS'   : '1.01',
         #'Vg'    : '1.01' ,
         #'WpWpJJ': '1.01' ,
         #'WpWpJJ_QCD': '1.01' ,
    #}, 
#} 


#nuisances['pdf_gg']  = {
               #'name'  : 'pdf_gg', 
               #'samples'  : {
                   #'DY' : '1.XX',
                   #'WpWpJJ': '1.XX',                   
                   #},
               #'type'  : 'lnN',
              #}


#nuisances['pdf_qqbar']  = {
               #'name'  : 'pdf_qqbar', 
               #'type'  : 'lnN',
               #'samples'  : {
                   #'lep_TT' : '1.XX',
                   #'Vg': '1.XX' ,
                   #},
              #}

#nuisances['pdf_gg_accept']  = {
               #'name'  : 'pdf_gg_accept', 
               #'samples'  : {
                   #'DY' : '1.XX',
                   #'WpWpJJ': '1.XX',                   
                   #},
               #'type'  : 'lnN',
              #}


#nuisances['pdf_qqbar_accept']  = {
               #'name'  : 'pdf_qqbar_accept', 
               #'type'  : 'lnN',
               #'samples'  : {
                   #'lep_TT' : '1.XX',
                   #'Vg': '1.XX' ,
                   #},
              #}


#    
#    
#    
#    














# experimental uncertainties


# FIXME: to be added and split
# - lepton resolution
# - pileup


## nuisances handled by means of a weight in the tree

#nuisances['pileup']  = {
                #'name'  : 'pileup', 
                #'kind'  : 'weight',
                #'type'  : 'shape',
                #'samples'  : {
                   ##'ttbar' : ['puWup/puW', 'puWdown/puW'],
                   ##'DY'    : ['puWup/puW', 'puWdown/puW']
                   #'ttbar' : ['3./puW', '0.3/puW'],
                   #'DY'    : ['3./puW', '0.3/puW']
                #}
#}


# fakes 


nuisances['fake_syst']  = {
               'name'  : 'fake_syst', 
               'type'  : 'lnN',
               'samples'  : {
                   'Fake' : '1.30',
                   },
}
 

# FIXME : restore it once we have the niusance ready                                 

#nuisances['fake_ele']  = {
                #'name'  : 'fake_ele_hww',
                #'kind'  : 'weight',
                #'type'  : 'shape',
                #'samples'  : {
                   #'Fake'      : ['fakeW2l2jElUp/fakeW2l2j',
                                  #'fakeW2l2jElDown/fakeW2l2j'],
                #}
#}
 

#nuisances['fake_ele_stat']  = {
                #'name'  : 'fake_ele_stat',
                #'kind'  : 'weight',
                #'type'  : 'shape',
                #'samples'  : {
                   #'Fake'      : ['fakeW2l2jstatElUp/fakeW2l2j',
                                  #'fakeW2l2jstatElDown/fakeW2l2j'],
                #}
#}


#nuisances['fake_mu']  = {
                #'name'  : 'fake_mu_hww',
                #'kind'  : 'weight',
                #'type'  : 'shape',
                #'samples'  : {
                   #'Fake'      : ['fakeW2l2jMuUp/fakeW2l2j',
                                  #'fakeW2l2jMuDown/fakeW2l2j'],
                #}
#}
 

#nuisances['fake_mu_stat']  = {
                #'name'  : 'fake_mu_stat',
                #'kind'  : 'weight',
                #'type'  : 'shape',
                #'samples'  : {
                   #'Fake'      : ['fakeW2l2jstatMuUp/fakeW2l2j',
                                  #'fakeW2l2jstatMuDown/fakeW2l2j'],
                #}
#}


# others ... 
  
                                 
# FIXME : restore it once we have the niusance ready                                 
  
#nuisances['btag']  = {
                #'name'  : 'ICHEP_btag',
                #'kind'  : 'weight',
                #'type'  : 'shape',
                #'samples'  : {
                   #'DY' : ['(bPogSFUp)/(bPogSF)', '(bPogSFDown)/(bPogSF)'],
                   #'lep_TT' : ['(bPogSFUp)/(bPogSF)', '(bPogSFDown)/(bPogSF)'],
                   #'Vg'  : ['(bPogSFUp)/(bPogSF)', '(bPogSFDown)/(bPogSF)'],
                   #'WZ'  : ['(bPogSFUp)/(bPogSF)', '(bPogSFDown)/(bPogSF)'],
                   #'WpWpJJ'   : ['(bPogSFUp)/(bPogSF)', '(bPogSFDown)/(bPogSF)'],
                #}
#}
 
 
nuisances['btagbc']  = {
                'name'  : 'ICHEP_btag_bc',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'chargeMisId' : ['(bPogSF_CSVM_bc_up)/(bPogSF)', '(bPogSF_CSVM_bc_down)/(bPogSF)'],
                   'Vg'  : ['(bPogSF_CSVM_bc_up)/(bPogSF)', '(bPogSF_CSVM_bc_down)/(bPogSF)'],
                   'WZ'  : ['(bPogSF_CSVM_bc_up)/(bPogSF)', '(bPogSF_CSVM_bc_down)/(bPogSF)'],
                   'ZZ'  : ['(bPogSF_CSVM_bc_up)/(bPogSF)', '(bPogSF_CSVM_bc_down)/(bPogSF)'],
                   'VVV'  : ['(bPogSF_CSVM_bc_up)/(bPogSF)', '(bPogSF_CSVM_bc_down)/(bPogSF)'],
                   'DPS'  : ['(bPogSF_CSVM_bc_up)/(bPogSF)', '(bPogSF_CSVM_bc_down)/(bPogSF)'],
                   'WpWpJJ'   : ['(bPogSF_CSVM_bc_up)/(bPogSF)', '(bPogSF_CSVM_bc_down)/(bPogSF)'],
                   'WpWpJJ_QCD'   : ['(bPogSF_CSVM_bc_up)/(bPogSF)', '(bPogSF_CSVM_bc_down)/(bPogSF)'],
                }
}
 

nuisances['btagudsg']  = {
                'name'  : 'ICHEP_btag_udsg',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'chargeMisId' : ['(bPogSF_CSVM_udsg_up)/(bPogSF)', '(bPogSF_CSVM_udsg_down)/(bPogSF)'],
                   'Vg'  : ['(bPogSF_CSVM_udsg_up)/(bPogSF)', '(bPogSF_CSVM_udsg_down)/(bPogSF)'],
                   'WZ'  : ['(bPogSF_CSVM_udsg_up)/(bPogSF)', '(bPogSF_CSVM_udsg_down)/(bPogSF)'],
                   'ZZ'  : ['(bPogSF_CSVM_udsg_up)/(bPogSF)', '(bPogSF_CSVM_udsg_down)/(bPogSF)'],
                   'VVV'  : ['(bPogSF_CSVM_udsg_up)/(bPogSF)', '(bPogSF_CSVM_udsg_down)/(bPogSF)'],
                   'DPS'  : ['(bPogSF_CSVM_udsg_up)/(bPogSF)', '(bPogSF_CSVM_udsg_down)/(bPogSF)'],
                   'WpWpJJ'   : ['(bPogSF_CSVM_udsg_up)/(bPogSF)', '(bPogSF_CSVM_udsg_down)/(bPogSF)'],
                   'WpWpJJ_QCD'   : ['(bPogSF_CSVM_udsg_up)/(bPogSF)', '(bPogSF_CSVM_udsg_down)/(bPogSF)'],
                }
} 
  
 
# FIXME : restore it once we have the niusance ready                                 
#         but it is still a negligible nuisance
  
## DY pt corrections
#nuisances['DYptRew']  = {
                #'name'  : 'DYptRew',   # Theory uncertainty
                #'kind'  : 'weight',
                #'type'  : 'shape',
                #'samples'  : {  # up              down
                   #'DY'     : ['(0.95 - 0.1*TMath::Erf((gen_ptll-14.4)/9.0))/(0.95 - 0.1*TMath::Erf((gen_ptll-14)/8.8))',
                               #'(0.95 - 0.1*TMath::Erf((gen_ptll-13.6)/8.6))/(0.95 - 0.1*TMath::Erf((gen_ptll-14)/8.8))'],
                #}
                ## tt = 17/18/19 depending on the sample/generator
                ## tW = 15/16
                
#}

##
##         1  p0           1.42199e+01   2.00614e-01   7.49397e-04  -3.24175e-03
##         2  p1           8.78770e+00   2.36675e-01   1.47925e-03  -1.11709e-03
##  
##      (0.95 - 0.1*TMath::Erf((x-14)/8.8))
##


  

nuisances['trigg']  = {
                'name'  : 'trigger',
                'kind'  : 'weight',
                #'kind'  : 'tree', #'weight',
                'type'  : 'shape',
                'samples'  : {
                   'chargeMisId' : ['(effTrigW_Up)/(effTrigW)', '(effTrigW_Down)/(effTrigW)'],
                   'Vg'  : ['(effTrigW_Up)/(effTrigW)', '(effTrigW_Down)/(effTrigW)'],
                   'WZ'  : ['(effTrigW_Up)/(effTrigW)', '(effTrigW_Down)/(effTrigW)'],
                   'ZZ'  : ['(effTrigW_Up)/(effTrigW)', '(effTrigW_Down)/(effTrigW)'],
                   'VVV'  : ['(effTrigW_Up)/(effTrigW)', '(effTrigW_Down)/(effTrigW)'],
                   'DPS'  : ['(effTrigW_Up)/(effTrigW)', '(effTrigW_Down)/(effTrigW)'],
                   'WpWpJJ': ['(effTrigW_Up)/(effTrigW)', '(effTrigW_Down)/(effTrigW)'],
                   'WpWpJJ_QCD': ['(effTrigW_Up)/(effTrigW)', '(effTrigW_Down)/(effTrigW)'],
                },
                #'folderUp'   : 'eos/user/a/amassiro/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__TrigEff/',    # uncertainties fixed!
                #'folderDown' : 'eos/user/a/amassiro/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__TrigEff/' 
}




# FIXME : restore it once we have the niusance ready                                 

nuisances['idiso_ele']  = {
                'name'  : 'idiso_ele',
                'kind'  : 'weight',
                #'kind'  : 'tree', #'weight',
                'type'  : 'shape',
                'samples'  : {
                   'chargeMisId' : ['((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))', '((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))'],
                  'Vg' : ['((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))', '((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))'],
                  'WZ' : ['((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))', '((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))'],
                  'ZZ' : ['((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))', '((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))'],
                  'VVV' : ['((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))', '((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))'],
                  'DPS' : ['((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))', '((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))'],
                  'WpWpJJ' : ['((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))', '((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))'],
                  'WpWpJJ_QCD' : ['((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))', '((abs(std_vector_lepton_flavour[0]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 13)) * ((abs(std_vector_lepton_flavour[1]) == 11)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 13))'],
                 },
                #'folderUp'   : 'eos/user/a/amassiro/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__TrigEff/',    # uncertainties fixed!
                #'folderDown' : 'eos/user/a/amassiro/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__TrigEff/' 
}
                

nuisances['idiso_mu']  = {
                'name'  : 'idiso_mu',
                'kind'  : 'weight',
                #'kind'  : 'tree', #'weight',
                'type'  : 'shape',
                'samples'  : {

                   'chargeMisId' : ['((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))', '((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))'],
                  'Vg' : ['((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))', '((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))'],
                  'WZ' : ['((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))', '((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))'],
                  'ZZ' : ['((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))', '((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))'],
                  'VVV' : ['((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))', '((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))'],
                  'DPS' : ['((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))', '((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))'],
                  'WpWpJJ' : ['((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))', '((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))'],
                  'WpWpJJ_QCD' : ['((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Up[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))', '((abs(std_vector_lepton_flavour[0]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[0])/(std_vector_lepton_idisoWcut_WP_Tight80X[0])+(abs(std_vector_lepton_flavour[0]) == 11)) * ((abs(std_vector_lepton_flavour[1]) == 13)*(std_vector_lepton_idisoWcut_WP_Tight80X_Down[1])/(std_vector_lepton_idisoWcut_WP_Tight80X[1])+(abs(std_vector_lepton_flavour[1]) == 11))'],
                },
                #'folderUp'   : 'eos/user/a/amassiro/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__TrigEff/',    # uncertainties fixed!
                #'folderDown' : 'eos/user/a/amassiro/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__TrigEff/' 
}


                

# nuisances handled by means of a different set of trees

# FIXME : restore it once we have the niusance ready                                 

nuisances['jes']  = {
                'name'  : 'scale_j', 
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'chargeMisId' :['1', '1'],
                   'Vg' :  ['1', '1'],
                   'WZ' : ['1', '1'],
                   'ZZ' : ['1', '1'],
                   'VVV' : ['1', '1'],
                   'DPS' : ['1', '1'],
                   'WpWpJJ' :  ['1', '1'],
                   'WpWpJJ_QCD' :  ['1', '1'],
                },


                'folderUp'   :'/pnfs/iihe/cms/store/user/xjanssen/HWW2015/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__JESup__tightVbsSel/',
                'folderDown' :'/pnfs/iihe/cms/store/user/xjanssen/HWW2015/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__JESdo__tightVbsSel/' 


                #'folderUp'   : 'eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWTightMu/07Jun2016_spring16_mAODv2_4p0fbm1/MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxup/',
                #'folderDown' : 'eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWTightMu/07Jun2016_spring16_mAODv2_4p0fbm1/MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxdo/' 

                #'folderUp'   : 'eos/user/r/rebeca/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxup/',
                #'folderDown' : 'eos/user/r/rebeca/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxdo/' 
                #'folderUp'   : 'eos/user/j/jlauwers/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxup/',
                #'folderDown' : 'eos/user/j/jlauwers/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxdo/' 
                #'folderUp'   : 'eos/user/j/jlauwers/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__JESup/',
                #'folderDown' : 'eos/user/j/jlauwers/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__JESdo/' 
                #'folderUp'   : 'eos/user/a/amassiro/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__JESup/',
                #'folderDown' : 'eos/user/a/amassiro/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__JESdo/' 
}




# FIXME : restore it once we have the niusance ready                                 

nuisances['electronpt']  = {
                'name'  : 'scale_e', 
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'chargeMisId' :['1', '1'],
                   'Vg' :  ['1', '1'],
                   'WZ' : ['1', '1'],
                   'ZZ' : ['1', '1'],
                   'VVV' : ['1', '1'],
                   'DPS' : ['1', '1'],
                   'WpWpJJ' :  ['1', '1'],
                   'WpWpJJ_QCD' :  ['1', '1'],
                },
                                
                'folderUp'   :'/pnfs/iihe/cms/store/user/xjanssen/HWW2015/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__LepElepTCutdo__tightVbsSel/',
                'folderDown' :'/pnfs/iihe/cms/store/user/xjanssen/HWW2015/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__LepElepTCutdo__tightVbsSel/' 


                ##'folderUp'   : 'eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWTightMu/07Jun2016_spring16_mAODv2_4p0fbm1/MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTup/',
                ##'folderDown' : 'eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWTightMu/07Jun2016_spring16_mAODv2_4p0fbm1/MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTdo/' 
                ##'folderUp'   : 'eos/user/r/rebeca/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTup/',
                ##'folderDown' : 'eos/user/r/rebeca/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTdo/' 
                ##'folderUp'   : 'eos/user/j/jlauwers/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTup/',
                ##'folderDown' : 'eos/user/j/jlauwers/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTdo/' 
                ##'folderUp'   : 'eos/user/a/amassiro/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTup/',
                ##'folderDown' : 'eos/user/a/amassiro/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTdo/' 
}
                
# FIXME : restore it once we have the niusance ready                                 
   
nuisances['muonpt']  = {
                'name'  : 'scale_m', 
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'chargeMisId' :['1', '1'],
                   'Vg' :  ['1', '1'],
                   'WZ' : ['1', '1'],
                   'ZZ' : ['1', '1'],
                   'VVV' : ['1', '1'],
                   'DPS' : ['1', '1'],
                   'WpWpJJ' :  ['1', '1'],
                   'WpWpJJ_QCD' :  ['1', '1'],
                },
                
                'folderUp'   : '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__LepMupTCutup__tightVbsSel/',
                'folderDown' : '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__LepMupTCutdo__tightVbsSel/' 
                
                ##'folderUp'   : 'eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWTightMu/07Jun2016_spring16_mAODv2_4p0fbm1/MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTup/',
                ##'folderDown' : 'eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWTightMu/07Jun2016_spring16_mAODv2_4p0fbm1/MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTdo/' 
                ##'folderUp'   : 'eos/user/r/rebeca/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTup/',
                ##'folderDown' : 'eos/user/r/rebeca/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTdo/' 
                ##'folderUp'   : 'eos/user/j/jlauwers/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTup/',
                ##'folderUp'   : 'eos/user/j/jlauwers/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTup/',
                ##'folderDown' : 'eos/user/j/jlauwers/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTdo/' 
                ##'folderUp'   : 'eos/user/a/amassiro/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTup/',
                ##'folderDown' : 'eos/user/a/amassiro/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTdo/' 
}


# FIXME : restore it once we have the niusance ready                                 

nuisances['met']  = {
                'name'  : 'scale_met', 
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'chargeMisId' :['1', '1'],
                   'Vg' :  ['1', '1'],
                   'WZ' : ['1', '1'],
                   'ZZ' : ['1', '1'],
                   'VVV' : ['1', '1'],
                   'DPS' : ['1', '1'],
                   'WpWpJJ' :  ['1', '1'],
                   'WpWpJJ_QCD' :  ['1', '1'],
                },

                'folderUp'   : '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__METup__tightVbsSel/',
                'folderDown' : '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/Apr2017_summer16/lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__genMatchVariables__l2tightVBS__METdo__tightVbsSel/' 


                #'folderUp'   : 'eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWTightMu/07Jun2016_spring16_mAODv2_4p0fbm1/MCl2loose__hadd__bSFL2pTEff__l2tight__METup/',
                #'folderDown' : 'eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWTightMu/07Jun2016_spring16_mAODv2_4p0fbm1/MCl2loose__hadd__bSFL2pTEff__l2tight__METdo/' 
                #'folderUp'   : 'eos/user/r/rebeca/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__METup/',
                #'folderDown' : 'eos/user/r/rebeca/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__METdo/' 
                #'folderUp'   : 'eos/user/j/jlauwers/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__METup/',
                #'folderDown' : 'eos/user/j/jlauwers/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__METdo/' 
                #'folderUp'   : 'eos/user/a/amassiro/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__METup/',
                #'folderDown' : 'eos/user/a/amassiro/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__METdo/' 
}


                
                
# statistical fluctuation
# on MC/data
# "stat" is a special word to identify this nuisance
nuisances['stat']  = {
                # apply to the following samples: name of samples here must match keys in samples.py
               'samples'  : {
                   
                   'chargeMisId': {
                         'typeStat' : 'bbb',
                         #'keepNormalization' : '1'  # default = 0 -> 0=don't keep normalization
                         },
                    
                   'Vg': {
                         'typeStat' : 'bbb',
                         },
                    
                   'WZ': {
                         'typeStat' : 'bbb',
                         },

                   'ZZ': {
                         'typeStat' : 'bbb',
                         },
                   'VVV': {
                         'typeStat' : 'bbb',
                         },

                   'DPS': {
                         'typeStat' : 'bbb',
                         },
                   
                   'WpWpJJ': {
                         'typeStat' : 'bbb',
                         },
                   
                   'WpWpJJ_QCD': {
                         'typeStat' : 'bbb',
                         },

                   'Fake': {  # needed?
                         'typeStat' : 'bbb',
                         },
                   
                   'DY_promptSubtr': {  # needed?
                         'typeStat' : 'bbb',
                         },
                   
                   'lep_TT_promptSubtr': {  # needed?
                         'typeStat' : 'bbb',
                         },
                   
                   'singleTop_promptSubtr': {  # needed?
                         'typeStat' : 'bbb',
                         },
                   
                   'singleAntiTop_promptSubtr': {  # needed?
                         'typeStat' : 'bbb',
                         },
                   
                   'ggWWTo2L2Nu_promptSubtr': {  # needed?
                         'typeStat' : 'bbb',
                         },
                   
                   'WWTo2L2Nu_promptSubtr': {  # needed?
                         'typeStat' : 'bbb',
                         },
                   
                   'ZZ_promptSubtr': {  # needed?
                         'typeStat' : 'bbb',
                         },
                   
                   'WpWpJJ_promptSubtr': {  # needed?
                         'typeStat' : 'bbb',
                         },
                   
                   'WpWpJJ_QCD_promptSubtr': {  # needed?
                         'typeStat' : 'bbb',
                         },
                   
                   'VVV_promptSubtr': {  # needed?
                         'typeStat' : 'bbb',
                         },
                   
                   'DPS_promptSubtr': {  # needed?
                         'typeStat' : 'bbb',
                         },
                   
                   'WZ_promptSubtr': {  # needed?
                         'typeStat' : 'bbb',
                         },

                 },
               'type'  : 'shape'
              }



