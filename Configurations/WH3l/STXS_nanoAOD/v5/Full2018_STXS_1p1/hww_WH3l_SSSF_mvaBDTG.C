#include "TMVA/Reader.h"
#include "TTree.h"
#include "TSystem.h"
#include "TROOT.h"
#include "TString.h"
#include "TFile.h"
#include "TChain.h"


using namespace std;

namespace multidraw {
  extern thread_local TTree* currentTree;
}

TMVA::Reader* myreaderBDTGSSSF = new TMVA::Reader();
bool initialized = false;
TString name_temp = "";

float loc0_WH3l_dphilllmet    , loc_WH3l_dphilllmet                                              ;
float loc0_WH3l_mOSll[100]    , loc_WH3l_mOSll_min                                               ;
float loc0_WH3l_ptOSll[100]   , loc_WH3l_ptOSll_min                                              ;
float loc0_WH3l_drOSll[100]   , loc_WH3l_drOSll_min                                              ;
float loc0_WH3l_ptlll         , loc_WH3l_ptlll                                                   ;
float loc0_WH3l_dphilmet[100] , loc_WH3l_dphilmet_0  , loc_WH3l_dphilmet_1 , loc_WH3l_dphilmet_2 ;
float loc0_WH3l_ptWWW         , loc_WH3l_ptWWW                                                   ;
float loc0_WH3l_mtWWW         , loc_WH3l_mtWWW                                                   ;
float loc0_WH3l_mlll          , loc_WH3l_mlll                                                    ;
float loc0_PuppiMET_pt        , loc_PuppiMET_pt                                                  ;
float loc0_Lepton_pt[100]     , loc_Lepton_pt_0      , loc_Lepton_pt_1     , loc_Lepton_pt_2     ;
int loc0_CleanJet_jetIdx[100]   ,loc_CleanJet_jetIdx_0, loc_CleanJet_jetIdx_1;
float loc0_Jet_btagDeepB[100]  ,loc_Jet_btagDeepB_0, loc_Jet_btagDeepB_1;


float minFunc(float nom0, float nom1, float nom2){
    float minimal = 9999;
    if (nom0 > 0)
        minimal = nom0;
    if ((nom1 > 0) && (nom1 < minimal))
        minimal = nom1;
    if ((nom2 > 0) && (nom2 < minimal))
        minimal = nom2;
    return minimal;
}
float bVeto(float* Jet_btagDeepB, int CleanJet_jetIdx){
    if (CleanJet_jetIdx >=0)
        return Jet_btagDeepB[CleanJet_jetIdx];
    else
        return -2;
}


void initmyreaderBDTSSSF(TTree* tree){

tree->SetBranchAddress("WH3l_mOSll",&loc0_WH3l_mOSll);
tree->SetBranchAddress("WH3l_ptOSll",&loc0_WH3l_ptOSll);
tree->SetBranchAddress("WH3l_drOSll",&loc0_WH3l_drOSll);
tree->SetBranchAddress("WH3l_dphilmet",&loc0_WH3l_dphilmet);
tree->SetBranchAddress("WH3l_ptWWW",&loc0_WH3l_ptWWW);
tree->SetBranchAddress("WH3l_mtWWW",&loc0_WH3l_mtWWW);
tree->SetBranchAddress("Lepton_pt",&loc0_Lepton_pt);

tree->SetBranchAddress("Jet_btagDeepB",&loc0_Jet_btagDeepB);
tree->SetBranchAddress("CleanJet_jetIdx",&loc0_CleanJet_jetIdx);

myreaderBDTGSSSF->AddVariable("MinIf$( WH3l_mOSll[], WH3l_mOSll[Iteration$] > 0)",&loc_WH3l_mOSll_min);
myreaderBDTGSSSF->AddVariable("MinIf$( WH3l_ptOSll[], WH3l_ptOSll[Iteration$] > 0)",&loc_WH3l_ptOSll_min);
myreaderBDTGSSSF->AddVariable("MinIf$( WH3l_drOSll[], WH3l_drOSll[Iteration$] > 0)",&loc_WH3l_drOSll_min);
myreaderBDTGSSSF->AddVariable("Alt$(Jet_btagDeepB[CleanJet_jetIdx[0]],-2)",&loc_Jet_btagDeepB_0);
myreaderBDTGSSSF->AddVariable("Alt$(Jet_btagDeepB[CleanJet_jetIdx[1]],-2)",&loc_Jet_btagDeepB_1);
myreaderBDTGSSSF->AddVariable("WH3l_dphilmet[0]",&loc_WH3l_dphilmet_0);
myreaderBDTGSSSF->AddVariable("WH3l_dphilmet[1]",&loc_WH3l_dphilmet_1);
myreaderBDTGSSSF->AddVariable("WH3l_dphilmet[2]",&loc_WH3l_dphilmet_2);
myreaderBDTGSSSF->AddVariable("WH3l_ptWWW",&loc_WH3l_ptWWW);
myreaderBDTGSSSF->AddVariable("WH3l_mtWWW",&loc_WH3l_mtWWW);
myreaderBDTGSSSF->AddVariable("Alt$(Lepton_pt[0],0)",&loc_Lepton_pt_0);
myreaderBDTGSSSF->AddVariable("Alt$(Lepton_pt[1],0)",&loc_Lepton_pt_1);
myreaderBDTGSSSF->AddVariable("Alt$(Lepton_pt[2],0)",&loc_Lepton_pt_2);

myreaderBDTGSSSF->BookMVA("BDTG1","/afs/cern.ch/user/p/pyu/public/HWWAnalysis/FullRunII_WH3l/BDT_xmlfile/21Nov2019/TMVAClassification_2018SSSF.weights.xml");

}

float hww_WH3l_SSSF_mvaBDTG(int entry, int nclass){

    if(name_temp != multidraw::currentTree->GetCurrentFile()->GetName()){
        name_temp = multidraw::currentTree->GetCurrentFile()->GetName();
        initialized = false;
    }

    if (!initialized){
        delete myreaderBDTGSSSF;
        myreaderBDTGSSSF = new TMVA::Reader();
        initmyreaderBDTSSSF(multidraw::currentTree);
        initialized = true;
    }

    multidraw::currentTree->GetEntry(entry);

    loc_WH3l_mOSll_min  = minFunc( loc0_WH3l_mOSll[0], loc0_WH3l_mOSll[1], loc0_WH3l_mOSll[2] );
    loc_WH3l_ptOSll_min = minFunc( loc0_WH3l_ptOSll[0],loc0_WH3l_ptOSll[1],loc0_WH3l_ptOSll[2]);
    loc_WH3l_drOSll_min = minFunc( loc0_WH3l_drOSll[0],loc0_WH3l_drOSll[1],loc0_WH3l_drOSll[2]);
    loc_Jet_btagDeepB_0 = bVeto(loc0_Jet_btagDeepB, loc0_CleanJet_jetIdx[0]);
    loc_Jet_btagDeepB_1 = bVeto(loc0_Jet_btagDeepB, loc0_CleanJet_jetIdx[1]);
    loc_WH3l_dphilmet_0 = loc0_WH3l_dphilmet[0] ;
    loc_WH3l_dphilmet_1 = loc0_WH3l_dphilmet[1] ;
    loc_WH3l_dphilmet_2 = loc0_WH3l_dphilmet[2] ;
    loc_WH3l_ptWWW      = loc0_WH3l_ptWWW      ;
    loc_WH3l_mtWWW      = loc0_WH3l_mtWWW      ;
    loc_Lepton_pt_0     = loc0_Lepton_pt[0]     ;
    loc_Lepton_pt_1     = loc0_Lepton_pt[1]     ;
    loc_Lepton_pt_2     = loc0_Lepton_pt[2]     ;

    float classifier = myreaderBDTGSSSF->EvaluateMVA("BDTG1");

    return classifier;

}

