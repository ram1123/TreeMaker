import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/00065901-3EEC-E611-8718-02163E019CD2.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/0474BC97-45EC-E611-8013-02163E019DA9.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/06C735FE-3DEC-E611-A491-02163E01A2BD.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/0A004B01-3EEC-E611-AD60-02163E014439.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/0A840BC4-4FEC-E611-BF84-02163E019C84.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/1EAF322E-3EEC-E611-8232-02163E011EF4.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/22960101-3EEC-E611-9868-02163E011BD0.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/22B14E02-3EEC-E611-BF9A-02163E014535.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/24CCDCFC-3DEC-E611-AAC0-02163E019C23.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/2A146899-45EC-E611-BA76-02163E019BA2.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/2AD3E4A9-4EEC-E611-868F-02163E019D26.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/30B3BE04-3EEC-E611-9E00-02163E01A6B2.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/327C2F00-3EEC-E611-850F-02163E01A700.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/364462FC-3DEC-E611-BF5A-02163E01A222.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/38ABD100-3EEC-E611-9EBB-02163E01A42F.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/3C89D5FC-3DEC-E611-BDD2-02163E019C19.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/3CC7FB87-35EC-E611-9A0C-02163E01A3F0.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/44F4A01D-3EEC-E611-9426-02163E011E31.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/4843BE16-3EEC-E611-BE9D-02163E01430B.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/48C4F003-3EEC-E611-BD56-02163E019E1C.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/48F476DC-45EC-E611-95D0-02163E0145FB.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/4A0AA28F-45EC-E611-BE46-02163E01A1C6.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/4C9DF696-45EC-E611-ABAF-02163E01A700.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/56C52600-3EEC-E611-B955-02163E01A396.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/5C622301-3EEC-E611-A8B2-02163E019CDC.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/640E6EC3-4FEC-E611-98C8-02163E011EF4.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/68FBF2FF-3DEC-E611-B800-02163E01459A.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/761AD2FD-3DEC-E611-8848-02163E019BEB.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/80243301-3EEC-E611-8891-02163E01A346.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/8C5C7997-45EC-E611-B30A-02163E019B92.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/92C5E405-3EEC-E611-9E28-02163E0139AA.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/9A4B2A00-3EEC-E611-94FA-02163E019DA8.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/9EEE02D3-45EC-E611-9501-02163E01439F.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/A8C154FC-3DEC-E611-9E43-02163E01A479.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/A8EE2C9F-45EC-E611-B47A-02163E019B6A.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/AA1FA514-3EEC-E611-8C68-02163E011AFB.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/AC7FC1C5-4FEC-E611-9574-02163E019E5B.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/AE730EFE-3DEC-E611-A414-02163E01A705.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/B2947314-3EEC-E611-B1C8-02163E01A255.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/BA0676C7-4FEC-E611-A411-02163E019BA3.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/BC7C61FD-3DEC-E611-978C-02163E019DA9.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/BE0A1E01-3EEC-E611-BA01-02163E01A377.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/BE86ABFC-3DEC-E611-93DB-02163E019BB5.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/C6538F02-3EEC-E611-8710-02163E019C3D.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/D28DC409-3EEC-E611-87FE-02163E0118F2.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/D8D662C9-45EC-E611-9AE6-02163E01346F.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/E077F300-3EEC-E611-B3FF-02163E019B6A.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/E0C09194-45EC-E611-A161-02163E013916.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/E6C7C48C-35EC-E611-86D8-02163E01A41B.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/E8CF3DA0-35EC-E611-9B00-02163E019D6D.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/100000/F42C41FE-3DEC-E611-9223-02163E01A365.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/00AAF5A3-DDEB-E611-BAF6-02163E01A21A.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/00B8EE34-E6EB-E611-8BB4-02163E01A21A.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/00F3B273-EEEB-E611-B5C9-02163E019DA3.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/021D5917-F6EB-E611-8817-02163E01A5B8.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/0270D1AA-DDEB-E611-8CE2-02163E01A1E1.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/041EEE2F-E6EB-E611-8F64-02163E01A50D.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/0C366449-F5EB-E611-ABD1-02163E019CBD.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/0E5A82A9-DDEB-E611-B447-02163E019B50.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/0EBC1236-E6EB-E611-B427-02163E019E44.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/1051E12F-E6EB-E611-8775-02163E019D41.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/127BB978-EEEB-E611-BDE6-02163E019D3E.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/12DFF677-EEEB-E611-A8D7-02163E01A286.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/1A6C85A6-DDEB-E611-8241-02163E019C22.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/1AB3A03B-E6EB-E611-8781-02163E01A559.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/1AD56D7B-FDEB-E611-99D8-02163E019B23.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/1C110338-E6EB-E611-8F3B-02163E019CC3.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/1C76E031-E6EB-E611-B59F-02163E019B50.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/1E4A07A2-DDEB-E611-9C5B-02163E01A50D.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/1EAFB139-E6EB-E611-BEDF-02163E01A4C9.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/225A6A59-F5EB-E611-9396-02163E011C43.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/28E71435-E6EB-E611-9DFB-02163E019E33.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/2A08F21A-F6EB-E611-BD49-02163E01A45C.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/36037372-EEEB-E611-8770-02163E019CB7.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/38277E99-04EC-E611-988A-02163E01A2FD.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/385E0C2F-E6EB-E611-998E-02163E01A6B2.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/3A691A74-D6EB-E611-A0B4-02163E01A3F0.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/403CB371-EEEB-E611-95A5-02163E019DE1.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/4270403F-EFEB-E611-8500-02163E019B9B.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/44D9AF41-EFEB-E611-8954-02163E019CDD.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/44FA9A2F-E6EB-E611-ABEB-02163E01A223.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/48134280-D6EB-E611-9000-02163E019E91.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/4872D0A4-DDEB-E611-8671-02163E01A65B.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/48D6FFA7-DDEB-E611-9D0E-02163E01A5ED.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/4A37666E-EEEB-E611-B185-02163E019E16.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/4CC84E32-E6EB-E611-8E94-02163E01A717.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/4E771830-E6EB-E611-909F-02163E01A379.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/54347D3A-E6EB-E611-BFE8-02163E019E03.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/5455DB19-F6EB-E611-9A8F-02163E01A491.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/56B5E530-E6EB-E611-B174-02163E01A582.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/56CE48E0-CEEB-E611-9317-02163E019C1E.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/584B1740-EFEB-E611-BB8D-02163E01A1BB.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/5A40C53A-E6EB-E611-B51A-02163E013518.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/5AF034A6-DDEB-E611-A741-02163E01A639.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/5C409C39-E6EB-E611-8F90-02163E019B86.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/607B9B70-EEEB-E611-B50F-02163E019B9C.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/62248240-F6EB-E611-87AC-02163E01A756.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/6673A435-E6EB-E611-B0F6-02163E01A26A.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/6A0FEDA0-DDEB-E611-BAB9-02163E019D38.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/702B2DA3-DDEB-E611-A6DA-02163E019D96.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/722C8A20-F6EB-E611-8A48-02163E011A08.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/74492F73-EEEB-E611-821C-02163E01A326.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/74DA7F30-E6EB-E611-B5DA-02163E01A65B.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/7699AF73-EEEB-E611-9D08-02163E01A1DE.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/7C6EEB75-EEEB-E611-9925-02163E019C3D.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/7E9B432E-E6EB-E611-A729-02163E019CFA.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/849B8A7D-D6EB-E611-90F2-02163E01A506.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/88C74FAD-EDEB-E611-9DD7-02163E01A363.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/8AA40F34-E6EB-E611-B64F-02163E01379C.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/8CB23E79-EEEB-E611-9F02-02163E01A346.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/92384082-FDEB-E611-88E9-02163E019D78.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/9295A823-F6EB-E611-B542-02163E019E58.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/92DAB130-E6EB-E611-B68A-02163E019C21.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/9601BB71-EEEB-E611-946B-02163E019C5E.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/96D3DF79-D6EB-E611-BF27-02163E01A200.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/98ECFD35-E6EB-E611-8B55-02163E01A5ED.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/9C08CF30-E6EB-E611-BFD4-02163E019B29.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/9E277B36-E6EB-E611-8103-02163E019E23.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/A2519E35-E6EB-E611-A292-02163E01A639.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/A4EEED32-E6EB-E611-9630-02163E019DEC.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/A678073E-EFEB-E611-AABF-02163E019B2B.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/A689C734-E6EB-E611-A92D-02163E019E70.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/A68FF079-D6EB-E611-874B-02163E01A3B1.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/A6EFEF31-F6EB-E611-AB04-02163E019BD7.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/A8B40835-E6EB-E611-838A-02163E019E2D.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/AA3958A3-DDEB-E611-9363-02163E01A618.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/AC00C1A8-DDEB-E611-A8BE-02163E01A731.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/AE55D17A-D6EB-E611-8B3C-02163E019C6D.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/AEAD8F46-EFEB-E611-BDB1-02163E01A61E.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/B2CF906A-EFEB-E611-99FF-02163E01359E.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/B4521887-EEEB-E611-B0EA-02163E011FC0.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/B87A8DC6-EFEB-E611-B648-02163E019B94.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/B8ECE3C6-EFEB-E611-B1C3-02163E01A1F0.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/BAA22E70-EEEB-E611-8F16-02163E01A42F.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/BAB8B7AA-DDEB-E611-A254-02163E019E16.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/BABB04A6-DDEB-E611-91E8-02163E01A66F.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/BADFA547-EFEB-E611-BD24-02163E011C47.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/BC6FFBCD-EFEB-E611-A0E6-02163E013449.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/BCB21171-EEEB-E611-9BAE-02163E019CDB.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/BEFC1ED0-EFEB-E611-91A1-02163E014446.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/C0D83733-E6EB-E611-A926-02163E019B5E.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/C6BA3F3F-EFEB-E611-86C5-02163E019B2F.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/CAA0AD74-EEEB-E611-B91B-02163E019E09.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/CC2B5B43-EFEB-E611-9E36-02163E019C1E.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/CC7D76CB-EFEB-E611-B9AB-02163E01A63F.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/CE18A173-EEEB-E611-A8C0-02163E01A740.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/D0511E3D-EFEB-E611-AE37-02163E019D0D.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/D8A62F37-E6EB-E611-BFEC-02163E01A3E4.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/DAEE581D-F6EB-E611-B404-02163E019DAA.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/DC0E2818-F6EB-E611-B03B-02163E019D0D.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/DC641D22-F6EB-E611-9BB7-02163E0140DD.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/DEDBFAC7-EFEB-E611-946C-02163E019D41.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/E663717C-EEEB-E611-ADAD-02163E011C43.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/EABD1730-E6EB-E611-89F5-02163E019C19.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/EC0A0A35-E6EB-E611-B399-02163E019E41.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/EC963B7D-D6EB-E611-8AB1-02163E019C3D.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/EE4F4CA5-DDEB-E611-987D-02163E019CBB.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/EE94527A-D6EB-E611-ABDB-02163E019CDD.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/EEF3D63B-F5EB-E611-A1AE-02163E019DBF.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/F051A832-E6EB-E611-A26A-02163E019CDD.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/F4A71B2E-E6EB-E611-B33E-02163E01A251.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/F80F1032-E6EB-E611-ABC3-02163E019D43.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/F8BC8F41-E6EB-E611-A82E-02163E01A778.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/FACBA835-E6EB-E611-955D-02163E01A373.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/FE56F828-F6EB-E611-9CD7-02163E01A1F0.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/110000/FE60C930-E6EB-E611-A24A-02163E019D7D.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/007B4AA2-B9EB-E611-9D22-02163E01A4FA.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/021FCCD7-B1EB-E611-8BA8-02163E01A2AD.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/0245037E-A9EB-E611-9468-02163E01A23F.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/0475E8B6-9AEB-E611-A445-02163E019DBC.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/04828CA5-B9EB-E611-884C-02163E019DDB.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/0696A111-8CEB-E611-B6A4-02163E019D6C.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/14E74617-8CEB-E611-8F4E-02163E019BA2.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/16753CF1-9AEB-E611-9534-02163E019C82.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/16CBCF94-A9EB-E611-91FF-02163E01415A.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/1A01F26F-A9EB-E611-8597-02163E01367A.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/1A0339F7-A1EB-E611-8199-02163E011BC3.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/1ADCE0E4-A1EB-E611-BFFB-02163E01348B.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/1CDED1DB-A1EB-E611-B9FD-02163E01A23F.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/1E3E02DB-A1EB-E611-BADF-02163E019CDD.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/1E5B3693-C0EB-E611-87CA-02163E019BEA.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/20B3F0D3-B1EB-E611-B586-02163E01A756.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/22C1C27C-A9EB-E611-B55C-02163E019DF9.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/2638798E-93EB-E611-8761-02163E019DAB.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/283253A1-B9EB-E611-B8AF-02163E019CBF.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/2A3F5291-C0EB-E611-8666-02163E019D25.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/2AD862F7-A1EB-E611-AD79-02163E01367A.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/2CA1C8A4-B9EB-E611-AE93-02163E019B61.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/34465C7E-A9EB-E611-85BA-02163E019B40.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/366A9219-B2EB-E611-AAAB-02163E01438E.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/383D7E15-8CEB-E611-8B36-02163E019CE3.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/3A4289DD-B1EB-E611-AA38-02163E019B40.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/3C213894-93EB-E611-A06E-02163E01A6BF.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/3C465543-A2EB-E611-AE26-02163E0145FB.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/3CA51DD5-B1EB-E611-8E5D-02163E01202B.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/3ECC3B7D-A9EB-E611-A703-02163E01A4F7.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/408DCBB6-9AEB-E611-BE8C-02163E01A223.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/42E81687-A9EB-E611-947E-02163E019BFA.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/4C2A19D6-B1EB-E611-8FE6-02163E01A6F5.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/54E849D6-A1EB-E611-A396-02163E019E2D.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/564DADD8-B1EB-E611-8232-02163E01A388.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/56CD61BB-9AEB-E611-99AC-02163E019BB1.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/5879CCA6-B9EB-E611-BF14-02163E01A6AF.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/58D844D7-B1EB-E611-91EE-02163E019DEA.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/607A3F77-A9EB-E611-85FC-02163E019B2B.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/62EFFEC2-9AEB-E611-90D0-02163E01A389.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/70EED359-A9EB-E611-A96F-02163E014387.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/72F348A0-B9EB-E611-A7ED-02163E019D25.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/80CEBBA3-B9EB-E611-856C-02163E019D10.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/82BFD3EE-C7EB-E611-9542-02163E019C1E.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/8454FCA6-B9EB-E611-9F31-02163E019DC8.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/886DBCAB-B9EB-E611-AC60-02163E019E8F.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/88E07A76-A9EB-E611-AD24-02163E01A51C.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/8A89F8E1-A1EB-E611-98EC-02163E019CD6.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/8E952ED7-B1EB-E611-AF29-02163E01A331.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/8EE1358E-93EB-E611-A2AE-02163E011D5C.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/90749B8E-C0EB-E611-B432-02163E019C3F.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/92291392-C0EB-E611-8B95-02163E01A1E1.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/92ABED85-93EB-E611-88F5-02163E019CB1.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/94012CE1-A1EB-E611-9243-02163E014387.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/98C2D876-A9EB-E611-9556-02163E01A388.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/98F1528E-93EB-E611-9EFA-02163E019E24.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/A20406B7-9AEB-E611-AD09-02163E0136B4.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/A613F5F0-C7EB-E611-BA51-02163E019C4A.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/A88DC383-A9EB-E611-8C5C-02163E019D4F.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/ACEE3B79-A9EB-E611-B360-02163E01A286.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/B071BBDD-B1EB-E611-8CE6-02163E01A429.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/B2F277C4-9AEB-E611-8375-02163E019D36.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/B4846BD6-A1EB-E611-842D-02163E019E2F.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/B83668A2-B9EB-E611-923C-02163E01A1E1.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/BC4AA99E-B9EB-E611-81DD-02163E019B85.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/BE2CC68C-C0EB-E611-9232-02163E019BB7.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/BE9BC7A0-B9EB-E611-945B-02163E019BB7.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/C6E9DEE3-9AEB-E611-B64B-02163E0140E6.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/D2E93478-A9EB-E611-A23A-02163E019B92.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/D6FC0077-A9EB-E611-885F-02163E01A6F5.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/D84A7214-8CEB-E611-921B-02163E019BB4.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/E285D99E-B9EB-E611-9960-02163E019B86.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/E2BCA3E1-B1EB-E611-96CB-02163E01A6AF.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/E49051DC-A1EB-E611-A220-02163E012BB5.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/F056FC7F-A9EB-E611-9220-02163E01202B.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/F0F502A2-B9EB-E611-999D-02163E01A6AD.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/F23FD0A6-B9EB-E611-8A5A-02163E011C00.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/F8306259-0AEC-E611-BBCC-02163E01A488.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/FAFE117C-A9EB-E611-BD84-02163E019C8A.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/50000/FE87925F-A9EB-E611-B923-02163E019CFA.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/80000/04A0C534-1EEC-E611-8E88-02163E019E2C.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/03Feb2017-v1/80000/3823D3E8-1DEC-E611-9570-02163E013916.root',
] )
