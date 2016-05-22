import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/08A515C0-9306-E611-A813-02163E0176B2.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0C19D3F1-ED03-E611-86A7-0025904B144A.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0E1F3A6C-4905-E611-AD0E-D8D385FF35F1.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1406BF36-9202-E611-966C-002590AC5074.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1470FE55-9202-E611-88FF-0025907BAD4A.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1884DA99-9102-E611-A7DE-0025905C2CE4.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1AD8A9DE-B802-E611-A14B-0CC47A009E24.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1E6235DF-F203-E611-AF41-0025905B859E.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1EBA149F-6305-E611-8F4D-0090FAA57340.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1EDC2BC8-1B04-E611-9AE0-008CFA197D14.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/1EE7353C-4402-E611-B469-0025904C63FA.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/22EA5AEA-DD06-E611-AEA6-0090FAA57E84.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/24903D07-1203-E611-B04F-5C260AFC8D10.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/282B0637-4402-E611-BA29-0025905C3E36.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2AAF2537-4402-E611-B06D-0025905C5430.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/32AD4F20-4402-E611-A476-0025905D1D02.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/34739A97-9102-E611-8BD2-0025905C9740.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/347489B2-9705-E611-AE6F-002590D0AFEC.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3660E7BF-7005-E611-A84C-00259073E38A.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/38027F9D-9102-E611-9A14-0025904C6224.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3C83D7A4-6305-E611-A0C8-0090FAA57BA0.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/4207C834-5B03-E611-8CE3-0002C94CD13C.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/4ED49690-FB04-E611-BD77-008CFA197DA4.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/4ED86838-4402-E611-84B4-0025905C3D96.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/564A1984-EA03-E611-871F-000F53273750.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/5C44EB98-9102-E611-8DC7-0025905C2CE6.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/5C85C245-B005-E611-865E-002590E2F8B6.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/602F99CE-7005-E611-8D30-00259073E470.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/6211AD72-D004-E611-B2B6-02163E016136.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/66423EF8-F303-E611-9198-0090FAA57F24.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/6C480929-9302-E611-84E1-008CFA0648E0.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/742A28D7-E903-E611-91E6-1CC1DE18CFDE.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/7E54FE99-9102-E611-809F-0025904C66F4.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/7E8D3483-EC03-E611-9877-549F3525A200.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/84018678-B902-E611-BB83-001E6757CD34.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/86C4E5F4-DC06-E611-BAB7-02163E012EC7.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/880E6D9E-A205-E611-8D3C-001E67396E05.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/94F14B37-4402-E611-9D47-0025905C431A.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/960EE7E6-5B03-E611-A3E7-001E67DDC88A.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/96B99E8A-1205-E611-B298-549F3525B154.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/9CCA2E8A-EA03-E611-B31B-0CC47A57CCF4.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/9E3D7925-B902-E611-8AE7-002590D60000.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/A220585E-D604-E611-8A1F-0025905C2CE6.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/ACB4AC2A-EB03-E611-AD3E-008CFA197D10.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/AEAF0313-3906-E611-9DDE-001F296564FE.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/B2EE2397-9206-E611-A707-782BCB1612C0.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/B6ADAEAC-5C06-E611-92B5-0090FAA58D04.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/B867C7C9-7005-E611-BC6C-0090FAA58974.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/BA138A8D-C904-E611-A333-5065F38122D1.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/BA225A36-4402-E611-8BD3-0025904CDDFA.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/BE374659-8F02-E611-B67B-002590DE39F0.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/BE42E9B0-BB02-E611-ABA8-008CFA56D870.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/C46BE299-9102-E611-8706-0025905C53DE.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/C6F13CA3-9102-E611-9C4B-0025905C54BA.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/CAA17DBB-9005-E611-B0A0-02163E0141C9.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/D039ABCA-1203-E611-8E93-549F35AE4FE3.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/D09F5D3B-4402-E611-8473-0025905C42A8.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/D2F9A099-9102-E611-B507-0025905C2CD0.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/D4959098-9102-E611-A571-0025904C6626.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/D8E47D9C-EB04-E611-BF2F-002590D9D8BA.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/DC87E8DE-ED03-E611-B9C2-0025905D1D78.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/E2831A80-9202-E611-8FA3-549F35AC7E3C.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/F497BD99-9102-E611-BC7A-0025904C6626.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/FADD40E0-E803-E611-958D-44A84225C8DB.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/FE21339A-9102-E611-A51A-0025905C53A6.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/FEEBBC8E-FB04-E611-B55A-000F53273758.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/0094CBE4-6B03-E611-8465-0025901D4D54.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/02A228E8-6A02-E611-ABA7-0025904C6622.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/04A154A7-6A02-E611-9D2C-0025905C5486.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/088ACA6F-1702-E611-95CB-F45214939090.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/16997CD5-3C02-E611-A80B-0025905C96E8.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/22173085-1C03-E611-A68A-842B2B76653D.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/389FB90B-6A02-E611-8446-0025904B7C40.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/526B1A8D-6A02-E611-B6FC-0025905C96EA.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/5A2D0669-6A02-E611-9FD4-0025904C650A.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/5E579F2E-6A02-E611-9B8B-0025905C4264.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/90613792-1402-E611-AFBA-90B11CBCFFA9.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/90FD1805-3802-E611-A086-0CC47A009258.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/9E52B2C6-6A02-E611-B022-0025905C431A.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/A4991A30-6A02-E611-8ED3-0025905D1CAE.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/ACF96934-C603-E611-AE16-0025905C2C86.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/BAC94B5E-6A02-E611-9C25-0025904C5180.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/C2C4D922-6A02-E611-8487-0025904C6622.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/C8D80C04-5601-E611-B12C-0025904C51D8.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/C8D82AA3-6A02-E611-85D4-0025904C5180.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/F4EE33DE-3A01-E611-9512-002481DE4AA6.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/F8A60B59-ED03-E611-A5ED-002590DB91CE.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/20000/F8F99DD5-3C02-E611-B249-0025905C3D40.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/002A3B7E-3C02-E611-AC09-0025905C54C4.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/04F6DF5C-8303-E611-91D7-0025905C2D98.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/162509CD-8B02-E611-B97B-0025905C2CBC.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/1A47C971-8D02-E611-9AD6-0025905D1D50.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/1EA7AD1F-8D02-E611-AF3B-0025905C54C4.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/24AE768A-8D02-E611-8F48-0025905C54F6.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/285C2D18-8D02-E611-90DB-0025905C5484.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/2AC9C97B-3C02-E611-B181-0025905C54C4.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/3002894A-8D02-E611-B5A0-0025905C2CD0.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/3487146D-8D02-E611-8E57-0025905C5486.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/34DB357B-3C02-E611-8E42-003048947BBB.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/3AC7F167-8D02-E611-A940-0025905C54DA.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/425D2078-8D02-E611-96A6-0025905BA736.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/4661E933-8D02-E611-A124-0025904C516C.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/4AD3587C-3C02-E611-9A2F-0025904C6416.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/4EAD3660-8D02-E611-900D-0025905C3DCE.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/584133AD-B105-E611-9622-002590DB9152.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/5E87F763-8B05-E611-A829-002590DB052A.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/64A04DCE-8B02-E611-A847-0025905C5484.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/88359B94-3C02-E611-BCA8-0025905C53A6.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/8CD3C17B-3C02-E611-89C2-0025904CF766.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/8E75155F-8303-E611-8F43-0025904C51F2.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/9631F928-9403-E611-AF47-008CFA197980.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/9A63D27C-3C02-E611-83AC-0025904C6564.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/A0E0297A-3C02-E611-A12D-0025905C3E66.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/A88A8A52-8D02-E611-8C92-0025904C6226.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/A8CDE865-8D02-E611-8234-0025905C2CA6.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/B607EC7A-3C02-E611-92E2-0025905C2CD2.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/BE612B38-8D02-E611-BD22-0025905D1CB4.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/C623D47E-8D02-E611-9CE8-0025905C5502.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/CAB4A478-8D02-E611-9485-0025905C3D6A.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/CC75E76C-5004-E611-8BDE-00259048812E.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/CE57633F-9604-E611-BA45-0025904C6216.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/D247C57C-3C02-E611-9B50-0025905C53B0.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/D4FBF07C-3C02-E611-8644-0025904C66E6.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/DC1E917A-3C02-E611-8CEF-0025905C94D2.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/E0756513-8D02-E611-8931-0025905C2CBC.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/E866BC3B-8D02-E611-A778-0025905D1C56.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/E8A55D6A-8D02-E611-B830-0025905C2CA6.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/EA13391F-8D02-E611-B082-0025905C54BA.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/ECCD655E-8D02-E611-9DF3-0025905D1D00.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/F6F5B47E-3C02-E611-9BE9-0025904C641E.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/FC6AEA86-8D02-E611-AE57-0025904B7C42.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/FE7E5056-8D02-E611-8DFC-0025905C53A6.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/0497FA2C-F802-E611-A639-0025905C53DC.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/1E40F9F1-F802-E611-A327-0025904C540C.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/5AE39069-BE03-E611-9B72-002590DB9258.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/6A9823C5-B503-E611-80DE-0025904C669C.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/804A4143-F802-E611-AFA8-0025905C53B2.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/9A08A2F5-F802-E611-A9CF-0025905C975C.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/B84CCD01-6E03-E611-A671-0025904C4F9E.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/C244896B-DD02-E611-8C29-0025905C53DC.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/E0636F6B-DD02-E611-9FC6-0025905C2C84.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/EE697D06-B603-E611-9777-001E67A3F70E.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/F8639465-DD02-E611-8D71-0025905C3E68.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/FA09F048-DD02-E611-B517-0025904CF764.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/12045B6D-8603-E611-AB29-0090FAA569C4.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/1C6A35DB-4405-E611-B3C8-002590DE3A92.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/1E0FA655-6A02-E611-BEC9-0025904C67BA.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/225978F1-0C03-E611-BE35-0025902C9F3C.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/26167340-AB04-E611-A345-02163E01609A.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/307A2955-6A02-E611-8AA5-0025905C2CA6.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/32715B5E-F001-E611-AF5E-0025904C51F2.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/329C0368-F001-E611-AA2F-0025905C9742.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/38E0447D-F001-E611-BE82-0025905C54DA.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/4676B81D-D203-E611-951B-44A84225C7BB.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/4A3FC37E-1505-E611-A1AF-02163E017670.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/4CCAE2A6-DC04-E611-81C4-02163E017689.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/62F1A644-F001-E611-97B8-0025905C3E68.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/64CE1F54-6A02-E611-AA10-0025905C2CA6.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/64D946A9-C204-E611-8408-02163E013A94.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/6E675954-6A02-E611-ABD5-0025904C4E2A.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/761FA697-0003-E611-9F83-0025901A9EFC.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/827A4963-EC04-E611-B266-02163E013AB2.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/82C38C3A-F001-E611-98DD-0025904C66F2.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/8AE50636-6704-E611-9B88-00505602101C.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/98B09D36-EC04-E611-9ABA-02163E01780B.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/9A2404BD-AC04-E611-BA0D-02163E015E11.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/9CD05854-6A02-E611-A2B3-0025905C2CA6.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/A2780455-6A02-E611-A9DE-0025904C67BA.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/A6A89053-8203-E611-8D6E-0025905C4262.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/C03898B6-CA05-E611-907E-001E673986B5.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/C28A1C3B-C904-E611-BE34-02163E013F5F.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/C8A9118D-B402-E611-9412-002590747D94.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/CAF422E9-C905-E611-8016-002590DB91BE.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/CE7A1D54-6A02-E611-BCC0-0025905C2CA6.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/D4127FDA-AA04-E611-922B-02163E00C0B7.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/DACA1EF4-2404-E611-A24E-44A842CFC9BF.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/DC72225F-F001-E611-80B7-0025905C2CB8.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/E02A0C58-6A02-E611-89DE-0025904C67BA.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/E6BFCC56-6A02-E611-8030-0025904C67A6.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/E6C555D8-C905-E611-B38A-02163E013199.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/EA935E1F-E103-E611-B70E-D4AE526A092E.root',
       '/store/mc/RunIISpring16MiniAODv1/ZJetsToNuNu_HT-600To800_13TeV-madgraph/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/F014B233-EC04-E611-ABBF-02163E0178B8.root',
] )