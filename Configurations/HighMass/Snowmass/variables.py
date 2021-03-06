# variables

#variables = {}

cutdictSR = ['hww2l2v_13TeV_'+EMorEEorMM+'_0j', 'hww2l2v_13TeV_'+EMorEEorMM+'_1j', 'hww2l2v_13TeV_'+EMorEEorMM+'_2j', 'hww2l2v_13TeV_'+EMorEEorMM+'_ggh', 'hww2l2v_13TeV_'+EMorEEorMM+'_vbf']

#cutdictSRhigh = ['hww2l2v_13TeV_'+EMorEEorMM+'_high0j', 'hww2l2v_13TeV_'+EMorEEorMM+'_high1j', 'hww2l2v_13TeV_'+EMorEEorMM+'_high2j', 'hww2l2v_13TeV_'+EMorEEorMM+'_highggh', 'hww2l2v_13TeV_'+EMorEEorMM+'_highvbf']

#cutdictCR = ['hww2l2v_13TeV_'+EMorEEorMM+'_dy_0j', 'hww2l2v_13TeV_'+EMorEEorMM+'_dy_1j', 'hww2l2v_13TeV_'+EMorEEorMM+'_dy_2j', 'hww2l2v_13TeV_'+EMorEEorMM+'_dy_ggh', 'hww2l2v_13TeV_'+EMorEEorMM+'_dy_vbf', 'hww2l2v_13TeV_'+EMorEEorMM+'_top_0j', 'hww2l2v_13TeV_'+EMorEEorMM+'_top_1j', 'hww2l2v_13TeV_'+EMorEEorMM+'_top_2j', 'hww2l2v_13TeV_'+EMorEEorMM+'_top_ggh', 'hww2l2v_13TeV_'+EMorEEorMM+'_top_vbf', 'hww2l2v_13TeV_'+EMorEEorMM+'_dy_high0j', 'hww2l2v_13TeV_'+EMorEEorMM+'_dy_high1j', 'hww2l2v_13TeV_'+EMorEEorMM+'_dy_high2j', 'hww2l2v_13TeV_'+EMorEEorMM+'_dy_highggh', 'hww2l2v_13TeV_'+EMorEEorMM+'_dy_highvbf', 'hww2l2v_13TeV_'+EMorEEorMM+'_top_high0j', 'hww2l2v_13TeV_'+EMorEEorMM+'_top_high1j', 'hww2l2v_13TeV_'+EMorEEorMM+'_top_high2j', 'hww2l2v_13TeV_'+EMorEEorMM+'_top_highggh', 'hww2l2v_13TeV_'+EMorEEorMM+'_top_highvbf']


variables['events']  = {   'name': '1',
                        'range' : (1,0,2),
                        'xaxis' : 'events',
                        'fold' : 3
 #                       'cuts'  : cutdictCR
                        }

variables['mTi_binning']  = {   'name': 'mTi',
                        'range' : ([0,75,100,120,140,160,180,200,220,240,260,280,300,350,400,450,500,600,700,800,900,1000,1250,1500,1750,2000,2250,2500,3000],), # Note: Leaving this comma after the list is important!
                        'xaxis' : 'm_{reco} [GeV]',
                        'fold' : 3,
                        'divideByBinWidth' : 1,
                        'cuts'  : cutdictSR
                        }

variables['DNN_mth_binning']  = {   'name': 'DNN_mth_OTF',
                        'range' : ([0,150,175,200,225,250,280,320,360,400,450,500,550,625,700,800,900,1000,1100,1200,1300,1450,1600,1800,2000,2250,2500,2750,3000,3500],),
                        'xaxis' : 'DNN m_{T} [GeV]',
                        'fold' : 3,
                        'divideByBinWidth' : 1,
                        'cuts'  : cutdictSR
                        }

### Kinematics:
variables['pt1']  = {   'name': 'Lepton_pt[0]',
                        'range' : (20,0,200),
                        'xaxis' : 'p_{T} 1st lep. [GeV]',
                        'fold'  : 3
                        }

variables['pt2']  = {   'name': 'Lepton_pt[1]',
                        'range' : (20,0,100),
                        'xaxis' : 'p_{T} 2nd lep. [GeV]',
                        'fold'  : 3
                        }

variables['eta1']  = {  'name': 'Lepton_eta[0]',
                        'range' : (20,-3,3),
                        'xaxis' : '#eta 1st lep.',
                        'fold'  : 3
                        }

variables['eta2']  = {  'name': 'Lepton_eta[1]',
                        'range' : (20,-3,3),
                        'xaxis' : '#eta 2nd lep.',
                        'fold'  : 3
                        }

variables['jetpt1']  = {   'name': 'CleanJet_pt[0]',
                        'range' : (20,0,300),
                        'xaxis' : 'p_{T} 1st jet [GeV]',
                        'fold'  : 2
                        }

variables['jetpt2']  = {   'name': 'CleanJet_pt[1]',
                        'range' : (20,0,200),
                        'xaxis' : 'p_{T} 2nd jet [GeV]',
                        'fold'  : 2
                        }

variables['jeteta1']  = {  'name': 'CleanJet_eta[0]',
                        'range' : (20,-5,5),
                        'xaxis' : '#eta 1st jet',
                        'fold'  : 2
                        }

variables['jeteta2']  = {  'name': 'CleanJet_eta[1]',
                        'range' : (20,-5,5),
                        'xaxis' : '#eta 2nd jet',
                        'fold'  : 2
                        }

variables['mth']  = {   'name': 'mth',
                        'range' : (20,0,400),
                        'xaxis' : 'm_{T,ll+MET} [GeV]',
                        'fold' : 3
                        }

variables['mth-DY']  = {   'name': 'mth',
                        'range' : (12, 0, 60),
                        'xaxis' : 'm_{T,ll+MET} [GeV]',
                        'fold' : 3
                        }

variables['mTi']  = {   'name': 'mTi',
                        'range' : (30,0,600),
                        'xaxis' : 'm_{reco} [GeV]',
                        'fold' : 3
                        }

variables['mll']  = {   'name': 'mll',
                        'range' : (25, 0,500),
                        'xaxis' : 'm_{ll} [GeV]',
                        'fold' : 3
                        }

variables['ptll']  = {   'name': 'ptll',
                        'range' : (20, 0,300),
                        'xaxis' : 'p_{T,ll} [GeV]',
                        'fold' : 3
                        }

variables['pTWW']  = {   'name': 'pTWW',
                        'range' : (20, 0,300),
                        'xaxis' : 'p_{T,WW} [GeV]',
                        'fold' : 3
                        }

variables['mtw1']  = {   'name': 'mtw1',
                        'range' : (20, 0,400),
                        'xaxis' : 'm_{T,l1+MET} [GeV]',
                        'fold' : 3
                        }

variables['pfmet']  = { 
                        'name': 'MET_pt',
                        'range' : (20,0,300),
                        'xaxis' : 'PF MET [GeV]',
                        'fold'  : 3
                        }

variables['puppimet']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (20,0,300),
                        'xaxis' : 'PUPPI MET [GeV]',
                        'fold'  : 3
                        }

### VBF:
variables['mjj']  = {
                        'name': 'mjj',
                        'range' : (30,0,600),
                        'xaxis' : 'm_{jj} [GeV]',
                        'fold'  : 2
                        }

variables['detajj']  = {
                        'name': 'detajj',
                        'range' : (20,0,5),
                        'xaxis' : '#Delta#eta_{jj}',
                        'fold'  : 2
                        }

### HM cuts:
variables['back2back_OTF']  = {
                        'name': 'back2back_OTF',
                        'range' : (20,0,5),
                        'xaxis' : '#DeltaR^{-1}',
                        'fold'  : 2
                        }

variables['dphill']  = {
                        'name': 'dphill',
                        'range' : (20,0,3.141592),
                        'xaxis' : '#Delta#phi_{ll}',
                        'fold'  : 2
                        }

variables['dphilmet']  = {
                        'name': 'dphilmet',
                        'range' : (20,0,3.141592),
                        'xaxis' : 'min(#Delta#phi_{l,MET})',
                        'fold'  : 2
                        }

variables['dphilmet2']  = {
                        'name': 'dphilmet2',
                        'range' : (20,0,3.141592),
                        'xaxis' : '#Delta#phi_{l2,MET}',
                        'fold'  : 2
                        }

variables['ht']  = {   'name': 'Lepton_pt[0]+Lepton_pt[0]+PuppiMET_pt[0]',
                        'range' : (20,0,600),
                        'xaxis' : 'p_{T} 1st, 2nd lep. + PUPPI MET [GeV]',
                        'fold'  : 3
                        }

### Recoil corrected MET:
variables['puppimet_recoil']  = {
                        'name': 'METrecoil_OTF * (METrecoil_OTF>40) - 1.0 * (METrecoil_OTF<=40)',
                        'range' : (20,0,300),
                        'xaxis' : 'recoil corrected PUPPI MET [GeV]',
                        'fold'  : 2
                        }

