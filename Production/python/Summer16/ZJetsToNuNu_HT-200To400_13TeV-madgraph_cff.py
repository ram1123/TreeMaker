import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/029F6BD2-5AC9-E611-BD77-0025907DC9D6.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/084E1E5E-CCC8-E611-8356-008CFA197D88.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/101D3BE4-7FC8-E611-A99A-0025904A96BC.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/22B43B4D-7CC8-E611-BB3C-0CC47A6C1058.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/2AF03531-82C8-E611-943B-0CC47AA98F9A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/30B9BC6A-88C9-E611-9908-0090FAA57FA4.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/30EE383F-77C8-E611-84F1-24BE05BD4F61.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3830657A-51C9-E611-AD4E-02163E011456.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3831A103-F5C8-E611-85AB-002590E7E07A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/385BC00A-08CA-E611-A1F5-0CC47AB0BB0A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/38A209FD-81C8-E611-846C-FA163E388EB8.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3C1DEDFF-57C9-E611-8CB0-0026181D28EA.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/440E3436-50C9-E611-930A-5065F37D9171.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/480A8C77-06CA-E611-9ECE-141877410ACD.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5493E899-99C8-E611-8B8B-002590207984.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5A664087-06CA-E611-BA2C-008CFA111170.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5E402C23-7AC8-E611-89B5-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6442143B-AEC8-E611-9886-008CFA1974A0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6E4A0739-50C9-E611-A6EC-0CC47AD98F72.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6E5FBD1A-8BC8-E611-B215-90B11C1453E1.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/74392FCC-78C8-E611-96F5-5065F381E271.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/76B01FA4-7DC8-E611-BE86-02163E012DD7.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/78778CD0-7FC8-E611-B73A-1866DAEA7D94.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7E42EBF2-7DC8-E611-B16B-B083FED42488.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/84D8F670-06CA-E611-AE8A-0025907B4F08.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/86A8D192-CAC8-E611-8789-008CFA1974A0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/92F0AA19-7BC8-E611-B69B-001E675A690A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/94E106AB-7CC8-E611-82EC-90B11C0BB9FC.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/964ADBFE-BFC9-E611-AFC4-002590E7D5A6.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/982ABFAA-81C8-E611-80F8-001E67A3FF1F.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9A04FC63-54C9-E611-97E3-6CC2173BBD70.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A24E858F-76C8-E611-A3F6-5065F381E271.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AA10F978-E0C8-E611-8FD7-485B3989725A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AA64477D-8AC8-E611-8FB1-842B2B1815AA.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B0F3CD54-74C8-E611-BA47-5065F381E271.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B470FE73-06CA-E611-99C4-B8CA3A70A5E8.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B4DB9A9A-E3C8-E611-9A2F-00259021A3D2.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B8956E83-45C9-E611-9B1C-02163E011456.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E03F1B7C-83C8-E611-909D-5065F38172A1.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E430BAF9-E9C8-E611-BD6C-002590E7E07A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E4D13B89-F1C8-E611-9C50-0CC47ABAC11C.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/EA543705-79C8-E611-B644-B083FECFEF7D.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/08247482-67C9-E611-820B-008CFA5D2758.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/28C6E35A-67C9-E611-B0AE-C81F66B78749.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2C72826B-67C9-E611-9520-1C6A7A21B2DD.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/66422520-47C9-E611-9745-047D7B881D1E.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/72954F2F-82C8-E611-9E80-E0071B7AE500.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/88508346-3DC9-E611-812E-FA163E3C5807.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A405E26B-4CC9-E611-8112-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A6C2E8A0-4CC9-E611-92B4-02163E013C4D.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B2C4657D-67C9-E611-A0CD-0025905B85CA.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BA7844C9-67C9-E611-ABD1-00266CFEFF04.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C06AAD95-67C9-E611-80B1-0090FAA573F0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C250E5DB-6FC9-E611-95B6-001E675A690A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C2774B24-68C9-E611-ACAD-0CC47A1E0DC8.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/CC27C05F-67C9-E611-8A6E-0CC47A78A2F6.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E0923CAA-67C9-E611-BE86-FA163EB5B001.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E29EA2B8-67C9-E611-8704-20CF3027A5CC.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F27649FE-7FC8-E611-9053-FA163E0BD4C5.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/04D56403-A3C9-E611-A0FE-008CFA1C93FC.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0C86F16D-9DC9-E611-A119-1866DAEECFD0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0E433996-97C8-E611-917B-002590E3A024.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/1E89B6C0-6BC9-E611-B101-002590E7DFFC.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2486B7B7-A2C9-E611-8662-6CC2173BBAB0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/343090B8-9CC8-E611-91F0-002590EFF972.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/46DEC547-90C8-E611-98D4-0025904A9472.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5A3EE084-88C8-E611-AA17-5065F3812221.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5C506FA1-A0C8-E611-B02D-0CC47AACC8A0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5EBCF149-C1C8-E611-8ADD-001E675A6653.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5EF6DBE5-8DC8-E611-A106-5065F3818291.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/72C0FF91-5CC9-E611-9D2F-0090FAA57F14.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/74D3EC26-F8C8-E611-88AA-001E67DDC88A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/76F165E8-93C8-E611-92C6-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/82FA861E-63C9-E611-B230-D48564594FB4.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8A5A2EF2-8AC8-E611-99BE-5065F3812221.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8C6CE87D-C7C8-E611-ACE2-0026181D28F0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/90279F7F-5EC9-E611-980C-24BE05C4D8F1.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/98B75401-9AC8-E611-BE73-0CC47A6C1038.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A28CD3AF-69C9-E611-AFE9-002590AC4C24.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A8EBF85D-91C8-E611-A39B-E0071B745DC0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/BA5498B8-A2C9-E611-BBDB-008CFA008F50.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/CC631D2D-8DC9-E611-9864-002590D9D89C.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D40F3018-63C9-E611-B2D3-901B0E5427AE.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D877F6DF-AAC8-E611-BB05-0CC47AD99044.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E86C1C31-79C9-E611-91AB-0CC47AD98D00.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F4522D0E-A3C9-E611-A798-0026181D28EA.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F488E1C1-55C9-E611-9EF7-02163E0130AE.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F48A8006-5CC9-E611-B0D2-02163E012D9E.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F819E076-95C8-E611-AE53-0CC47AD98D10.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/02077677-85C8-E611-80F3-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0E0D1530-7AC9-E611-A67F-008CFA0020D4.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/104F1B06-55C9-E611-A3FE-001E67A3F70E.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/18DE9286-7BC8-E611-B7ED-0CC47A13CDA0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/1A6B24B1-39C9-E611-9D24-00259073E3D2.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/229B2A21-A0C8-E611-950A-02163E019C2C.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3A9EFC14-55C9-E611-9313-A4BADB1CFD50.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/446E1CC6-54C9-E611-9F74-FA163E74CD2A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/46C28022-39C9-E611-8643-70106F45D198.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4A35E156-55C9-E611-B4FD-0025901D4C98.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4C81FA93-8EC8-E611-872A-02163E019DC3.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/58D2CBEA-81C8-E611-9B68-0CC47AA99438.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/5EBF3545-33C9-E611-AD4A-001E67A406E0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/5EC61349-4FC9-E611-8B32-E0071B7AC700.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/7E05D229-56C9-E611-A645-00259048AC9A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/7E65E54D-55C9-E611-91A3-0025907B5038.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/84770E26-4BC9-E611-8459-001E67504C05.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/88395E64-51C9-E611-B4DB-002590E7D5AE.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/888CB9F3-54C9-E611-A055-008CFA197E0C.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/BE4D0DD6-54C9-E611-925B-0CC47AA992D0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/BEEEF6FA-36C9-E611-9130-02163E012FE6.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D868C8F3-41C9-E611-85B4-6CC2173BC0B0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E65DC503-55C9-E611-9A11-02163E019C7F.root',
] )
