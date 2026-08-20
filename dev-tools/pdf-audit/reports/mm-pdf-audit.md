# MM 2024 PDF terminology audit

## Summary

- Missing Spanish entries: 0
- Extra Spanish entries: 0
- Invalid internal references: 0
- Macro mutation candidates: 0
- Reviewed command differences: 51
- Visible English terminology residues: 0
- Deprecated Spanish terminology occurrences: 0
- Probable untranslated English fields: 0

## Pack structure

| Pack | English | Spanish | Missing | Extra |
|---|---:|---:|---:|---:|
| actors | 504 | 504 | 0 | 0 |
| content | 8 | 8 | 0 | 0 |
| features | 680 | 680 | 0 | 0 |
| tables | 116 | 116 | 0 | 0 |

## Invalid internal references


## Macro mutation candidates


## Reviewed command differences

- `actors:entries.mmAncientGoldDra.items.mmMultiattack000.description`: kind=command-difference, removed=['[[/item]]', '[[/item]]'], added=['[[/item Spellcasting]]'], reviewCategory=source-command-correction, fingerprint=5410cb5293a473ca
- `actors:entries.mmEttercap000000.items.mmBite0000000000.effects.Mbzt84HngDw6JyWm.description`: kind=command-difference, removed=['[[lookup @name lowercase]]'], added=[], reviewCategory=localized-static-equivalent, fingerprint=62c6e1c2989b9d15
- `actors:entries.mmFaerieDragonAd.items.P6aIXlIJ6aMTJYdI.description`: kind=command-difference, removed=[], added=['[[lookup @name lowercase]]'], reviewCategory=spanish-automation-enhancement, fingerprint=4834cd46695352f4
- `actors:entries.mmFaerieDragonYo.items.RvZKaiCjENNT9evZ.description`: kind=command-difference, removed=[], added=['[[lookup @name lowercase]]'], reviewCategory=spanish-automation-enhancement, fingerprint=4834cd46695352f4
- `actors:entries.mmFireElemental0.items.mmWaterSusceptib.description`: kind=command-difference, removed=['[[lookup @name lowercase]]'], added=[], reviewCategory=localized-static-equivalent, fingerprint=62c6e1c2989b9d15
- `actors:entries.mmGelatinousCube.items.mmTransparent000.description`: kind=command-difference, removed=['[[lookup @name lowercase]]'], added=[], reviewCategory=localized-static-equivalent, fingerprint=62c6e1c2989b9d15
- `actors:entries.mmGiantElk000000.items.mmRam00000000000.description`: kind=command-difference, removed=[], added=['[[lookup @name lowercase]]'], reviewCategory=spanish-automation-enhancement, fingerprint=4834cd46695352f4
- `actors:entries.mmModronDuodrone.items.jbso67HYFgxJVoyJ.description`: kind=command-difference, removed=[], added=['[[lookup @name lowercase]]'], reviewCategory=spanish-automation-enhancement, fingerprint=4834cd46695352f4
- `actors:entries.mmMummyLord00000.items.Hp6Uq0ZvymMIEGys.description`: kind=command-difference, removed=['[[lookup @range.units activity=EsBmMUQMO4b0g6Yw]]', '[[lookup @target.affects.special activity=EsBmMUQMO4b0g6Yw]]', '[[lookup @target.template.size activity=EsBmMUQMO4b0g6Yw]]', '[[lookup @target.template.units activity=EsBmMUQMO4b0g6Yw]]'], added=['[[lookup @name lowercase]]'], reviewCategory=source-version-divergence, fingerprint=46e7c6f500f2a380
- `actors:entries.mmNightHag000000.items.q6QIeb22Jwvnb6cR.description`: kind=command-difference, removed=[], added=['[[lookup @name lowercase]]', '[[lookup @name lowercase]]'], reviewCategory=spanish-automation-enhancement, fingerprint=844ded7109e20e8c
- `actors:entries.mmNightmare00000.items.mmEtherealStride.description`: kind=command-difference, removed=['[[lookup @range.units activity=0EfvhIXAIPlYUiNE]]'], added=[], reviewCategory=localized-static-equivalent, fingerprint=2622332feae795d2
- `actors:entries.mmNoble000000000.items.vyPsPLDVgeQfiZcP.description`: kind=command-difference, removed=['[[lookup @prof]]'], added=[], reviewCategory=localized-static-equivalent, fingerprint=4e5cac0c15a06da2
- `actors:entries.mmNobleProdigy00.items.mmSpellcasting00.description`: kind=command-difference, removed=[], added=['[[lookup @name lowercase]]'], reviewCategory=spanish-automation-enhancement, fingerprint=4834cd46695352f4
- `actors:entries.mmNothic00000000.items.mmRottingGaze000.description`: kind=command-difference, removed=[], added=['[[lookup @damage.onSave capitalize activity=k4jetEkSCPApNFgz]]'], reviewCategory=spanish-automation-enhancement, fingerprint=c774c0a16f5cd681
- `actors:entries.mmNycaloth000000.items.mmShadowyTelepor.description`: kind=command-difference, removed=[], added=['[[lookup @name lowercase]]'], reviewCategory=spanish-automation-enhancement, fingerprint=4834cd46695352f4
- `actors:entries.mmOchreJelly0000.items.mmSplit000000000.description`: kind=command-difference, removed=['[[lookup @name lowercase]]', '[[lookup @name lowercase]]', '[[lookup @name lowercase]]', '[[lookup @name lowercase]]', '[[lookup @name capitalize]]'], added=[], reviewCategory=localized-static-equivalent, fingerprint=2ed8194d6683196b
- `actors:entries.mmPixieWonderbri.items.mmFaerieDust0000.effects.IYnaRAbPSikYHp99.description`: kind=command-difference, removed=[], added=['[[lookup @name lowercase]]'], reviewCategory=spanish-automation-enhancement, fingerprint=4834cd46695352f4
- `actors:entries.mmPixieWonderbri.items.mmFaerieDust0000.effects.CfdgxlE2FD4F1rL6.description`: kind=command-difference, removed=[], added=['[[lookup @name lowercase]]'], reviewCategory=spanish-automation-enhancement, fingerprint=4834cd46695352f4
- `actors:entries.mmPoltergeist000.items.mmTelekineticThr.description`: kind=command-difference, removed=['[[lookup @target.affects.labels.statblock activity=qHeMp7n2VPHtGbDS]]', '[[lookup @range.value activity=qHeMp7n2VPHtGbDS]]', '[[lookup @range.units activity=qHeMp7n2VPHtGbDS]]'], added=['[[lookup @range.special activity=qHeMp7n2VPHtGbDS]]'], reviewCategory=source-version-divergence, fingerprint=61fcc5315cc56e94
- `actors:entries.mmPoltergeist000.items.mmVanish00000000.description`: kind=command-difference, removed=[], added=['[[lookup @name lowercase]]'], reviewCategory=spanish-automation-enhancement, fingerprint=4834cd46695352f4
- `actors:entries.mmPoltergeist000.items.mmObjectSlam0000.description`: kind=command-difference, removed=[], added=['[[lookup @name lowercase]]'], reviewCategory=spanish-automation-enhancement, fingerprint=4834cd46695352f4
- `actors:entries.mmPriest00000000.items.mmSpellcasting00.description`: kind=command-difference, removed=[], added=['[[lookup @attributes.spell.dc]]'], reviewCategory=spanish-automation-enhancement, fingerprint=bc24204d96ab191b
- `actors:entries.mmSolar000000000.items.0lf6wzfUsp3jTIti.description`: kind=command-difference, removed=[], added=['[[/r 1d4*10]]'], reviewCategory=spanish-automation-enhancement, fingerprint=da88a91de4306678
- `actors:entries.mmYoungBlueDrago.items.mmLightningBreat.description`: kind=command-difference, removed=['[[lookup @target.template.type capitalize activity=LpjgVwftzGNMgTUJ]]'], added=[], reviewCategory=localized-static-equivalent, fingerprint=292bed319aa2e09f
- `features:entries.mmCataclysmicEve.effects.NNfBNxg6PO0NlffF.description`: kind=command-difference, removed=[], added=['[[/check ability=str skill=ath format=long]]'], reviewCategory=spanish-automation-enhancement, fingerprint=5102e13967fe2c72
- `features:entries.mmCorruptingTouc.description`: kind=command-difference, removed=['[[/attack extended]]', '[[/damage average extended]]'], added=['[[lookup @save.dc.value activity=F4cByCi1IEouN08a]]', '[[lookup @target.affects.labels.statblock activity=F4cByCi1IEouN08a]]', '[[lookup @name lowercase]]', '[[lookup @range.value activity=F4cByCi1IEouN08a]]', '[[/damage average]]'], reviewCategory=source-version-divergence, fingerprint=e209e14d38c5c5fe
- `features:entries.mmCounterattack0.description`: kind=command-difference, removed=[], added=['[[/item .cWEx0aUNtgAiphWk]]', '[[/item .UYIXz9iBOnpRuR1H]]'], reviewCategory=spanish-automation-enhancement, fingerprint=e1f1fb8df9565e12
- `features:entries.mmDrainingSwipe0.effects.6AjyMN83LppkkgC3.description`: kind=command-difference, removed=['[[/r 1d4]]'], added=[], reviewCategory=localized-static-equivalent, fingerprint=23e0b67993977dd0
- `features:entries.mmEruption000000.description`: kind=command-difference, removed=[], added=['[[/item .mmElementalBurst]]'], reviewCategory=spanish-automation-enhancement, fingerprint=6575646fb17e4f65
- `features:entries.mmEtherealStride.description`: kind=command-difference, removed=['[[lookup @range.units activity=0EfvhIXAIPlYUiNE]]'], added=[], reviewCategory=localized-static-equivalent, fingerprint=2622332feae795d2
- `features:entries.mmGnash000000000.description`: kind=command-difference, removed=[], added=['[[lookup @damage.onSave capitalize activity=CNoawEWxNhs5HRIk]]'], reviewCategory=spanish-automation-enhancement, fingerprint=f08e3af4d6e0c76b
- `features:entries.mmGraspingGlob00.description`: kind=command-difference, removed=[], added=['[[/item .mmRestrainingGlo]]'], reviewCategory=spanish-automation-enhancement, fingerprint=225c48465c9fd434
- `features:entries.mmHagsSwipe00000.description`: kind=command-difference, removed=[], added=['[[/item .mmSpectralClaw00]]'], reviewCategory=spanish-automation-enhancement, fingerprint=684e5240c0bd0251
- `features:entries.mmLashingGoop000.description`: kind=command-difference, removed=[], added=['[[/item .mmPseudopod00000]]'], reviewCategory=spanish-automation-enhancement, fingerprint=1472e3008bcf0e4a
- `features:entries.mmMagicRope00000.description`: kind=command-difference, removed=[], added=['[[/item .mmEntanglingRope]]'], reviewCategory=spanish-automation-enhancement, fingerprint=dd40a2713f2d43c1
- `features:entries.mmMindrendingRoa.description`: kind=command-difference, removed=['[[lookup @target.template.units activity=zPMfwwIoTFzIrN5H]]'], added=[], reviewCategory=localized-static-equivalent, fingerprint=a820dbe6ae109197
- `features:entries.mmOnslaught00000.description`: kind=command-difference, removed=[], added=['[[/item .mmClaw0000000000]]', '[[/item .mmTail0000000000]]'], reviewCategory=spanish-automation-enhancement, fingerprint=a337f23ad9de4b9f
- `features:entries.mmRavage00000000.description`: kind=command-difference, removed=['[[lookup @target.affects.special activity=TH3dFl51uS33f80l]]', '[[lookup @activation.condition activity=TH3dFl51uS33f80l]]'], added=['[[lookup @target.affects.special activity=Gi7NHst31Yf0KVM9]]', '[[lookup @activation.condition activity=Gi7NHst31Yf0KVM9]]', '[[/damage 2d8 slashing average]]'], reviewCategory=source-version-divergence, fingerprint=7095d7241b036a22
- `features:entries.mmReflexiveAnten.description`: kind=command-difference, removed=[], added=['[[/item .mmAntennae000000]]'], reviewCategory=spanish-automation-enhancement, fingerprint=e3e23b7b8d1815ba
- `features:entries.mmRottingGaze000.description`: kind=command-difference, removed=[], added=['[[lookup @damage.onSave capitalize activity=k4jetEkSCPApNFgz]]'], reviewCategory=spanish-automation-enhancement, fingerprint=c774c0a16f5cd681
- `features:entries.mmShadowyTelepor.description`: kind=command-difference, removed=[], added=['[[lookup @name lowercase]]'], reviewCategory=spanish-automation-enhancement, fingerprint=4834cd46695352f4
- `features:entries.mmSickeningRay00.description`: kind=command-difference, removed=['[[lookup @name lowercase]]'], added=['[[/attack extended]]', '[[/damage average extended]]'], reviewCategory=source-version-divergence, fingerprint=031fa8a3f5150674
- `features:entries.mmSlow0000000000.description`: kind=command-difference, removed=[], added=['[[lookup @attributes.spell.dc]]'], reviewCategory=spanish-automation-enhancement, fingerprint=bc24204d96ab191b
- `features:entries.mmSoulTome000000.description`: kind=command-difference, removed=[], added=['[[/item .mmBanishingClaw0]]'], reviewCategory=spanish-automation-enhancement, fingerprint=9457b95429b32b48
- `features:entries.mmStakeToTheHear.description`: kind=command-difference, removed=['[[lookup @name lowercase]]'], added=[], reviewCategory=localized-static-equivalent, fingerprint=62c6e1c2989b9d15
- `features:entries.mmStomp000000000.description`: kind=command-difference, removed=[], added=['[[/item Slam]]'], reviewCategory=spanish-automation-enhancement, fingerprint=8b605be250d6f28c
- `features:entries.mmSwarmOfGraspin.description`: kind=command-difference, removed=[], added=['[[lookup @activation.condition activity=hzeHzcSKHC4AvIJQ]]'], reviewCategory=spanish-automation-enhancement, fingerprint=57809d394b83c87b
- `features:entries.mmTelekineticThr.description`: kind=command-difference, removed=['[[lookup @target.affects.labels.statblock activity=qHeMp7n2VPHtGbDS]]', '[[lookup @range.value activity=qHeMp7n2VPHtGbDS]]', '[[lookup @range.units activity=qHeMp7n2VPHtGbDS]]'], added=['[[lookup @range.special activity=qHeMp7n2VPHtGbDS]]'], reviewCategory=source-version-divergence, fingerprint=61fcc5315cc56e94
- `features:entries.mmTransparent000.description`: kind=command-difference, removed=['[[lookup @name lowercase]]'], added=[], reviewCategory=localized-static-equivalent, fingerprint=62c6e1c2989b9d15
- `features:entries.mmUmbralStrike00.description`: kind=command-difference, removed=[], added=['[[/item .mmGraveStrike000]]', '[[/item .mmSickeningRay00]]'], reviewCategory=spanish-automation-enhancement, fingerprint=902b421822e7799f
- `features:entries.mmWaterSusceptib.description`: kind=command-difference, removed=['[[lookup @name lowercase]]'], added=[], reviewCategory=localized-static-equivalent, fingerprint=62c6e1c2989b9d15

## Visible English terminology findings


## Deprecated Spanish terminology


## Probable untranslated English fields
