#!/usr/bin/env python3
"""Apply reviewed translations for MM-specific residual English fields."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
COMPENDIUM = ROOT / "compendium"


ANIMAL_SPIRIT = (
    '<p>El [[lookup @name lowercase]] conjura un espíritu animal que golpea a una criatura y después desaparece.</p>'
    '<p><em>Tirada de salvación de Destreza:</em> CD [[lookup @save.dc.value activity=cx21u9ZYjSdu2m3U]], '
    'una criatura que el [[lookup @name lowercase]] pueda ver a [[lookup @range.value activity=cx21u9ZYjSdu2m3U]] pies.</p>'
    '<p><em>Fallo:</em> [[/damage average]] de daño.</p><p><em>Éxito:</em> La mitad del daño.</p>'
    '<p><em>Fallo o éxito:</em> Se produce uno de los siguientes efectos:</p>'
    '<p class="feature-trait"><strong>Fortificar (solo recolector).</strong> El [[lookup @name lowercase]] '
    'obtiene [[lookup @healing.formula activity=emHqEek8e9Mwyaj7]] puntos de golpe temporales.</p>'
    '<p class="feature-trait"><strong>Marcado como presa (solo cazador).</strong> El [[lookup @name lowercase]] '
    'tiene ventaja en las tiradas de ataque contra el objetivo hasta el comienzo del siguiente turno del '
    '[[lookup @name lowercase]].</p><p class="feature-trait"><strong>Enjambre molesto (solo sabio).</strong> '
    'El objetivo tiene desventaja en las tiradas de ataque y las pruebas de característica hasta el final de su siguiente turno.</p>'
)
LORDLY_PRESENCE = (
    '<p class="feature"><em>Tirada de salvación de Sabiduría:</em> CD [[lookup @save.dc.value activity=IlmzjggKrDB1c9dr]], '
    'cualquier [[lookup @target.affects.type activity=IlmzjggKrDB1c9dr]] que empiece su turno en una Emanación de '
    '[[lookup @target.template.size activity=IlmzjggKrDB1c9dr]] pies originada en el [[lookup @name lowercase]].</p>'
    '<p><em>Fallo:</em> El objetivo sufre uno de los siguientes efectos:</p>'
    '<p class="feature-trait"><strong>Cautivado (solo recolector).</strong> El objetivo tiene la condición '
    '&amp;Reference[Charmed apply=false]{Hechizado} hasta el final de su siguiente turno. Mientras está hechizado, '
    'también tiene la condición &amp;Reference[Incapacitated apply=false]{Incapacitado}.</p>'
    '<p class="feature-trait"><strong>Asustado (solo cazador).</strong> El objetivo tiene la condición '
    '&amp;Reference[Frightened apply=false]{Asustado} hasta el final de su siguiente turno.</p>'
    '<p class="feature-trait"><strong>Atascado (solo sabio).</strong> El objetivo recibe '
    '[[/damage average activity=hYhryWdKIuHOzmO3]] de daño y queda confundido mágicamente hasta el final de su '
    'siguiente turno. Mientras está confundido, resta [[/r 1d4]] de sus tiradas de salvación.</p>'
)


UPDATES: dict[str, dict[str, str]] = {
    "actors": {
        "entries.mmAncientBrassDr.items.mmSleepBreath000.effects.eiPsvHBjVi4pRHqJ.description":
            '<p>El objetivo tiene la condición &amp;Reference[Unconscious apply=false]{Inconsciente} durante la duración (consulta el objeto de origen para conocer la duración).</p>',
        "entries.mmAncientCopperD.items.mmGigglingMagic0.description":
            '<p class="feature"><em>Tirada de salvación de Carisma:</em> CD [[lookup @save.dc.value activity=Ttrajc4RC5Ut7pkj]], [[lookup @target.affects.labels.statblock activity=Ttrajc4RC5Ut7pkj]] que el [[lookup @name lowercase]] pueda ver a [[lookup @range.value activity=Ttrajc4RC5Ut7pkj]] pies.</p><p class="feature"><em>Fallo:</em> [[/damage average]] de daño. Hasta el final de su siguiente turno, el objetivo tira [[/r 1d8]] cuando realiza una prueba de característica o una tirada de ataque y resta el resultado de la prueba de D20.</p><p class="feature"><em>Fallo o éxito:</em> El [[lookup @name lowercase]] no puede volver a realizar esta acción hasta el inicio de su siguiente turno.</p>',
        "entries.mmAncientGoldDra.items.mmWeakeningBreat.description":
            '<p class="feature"><em>Tirada de salvación de Fuerza:</em> CD [[lookup @save.dc.value activity=EGZ4bS4HpJkfNG9s]], cada criatura que no esté afectada por este aliento en un Cono de [[lookup @target.template.size activity=EGZ4bS4HpJkfNG9s]] pies.</p><p class="feature"><em>Fallo:</em> El objetivo tiene desventaja en las pruebas de D20 basadas en Fuerza y resta 5 ([[/r 1d10]]) de sus tiradas de daño. Repite la salvación al final de cada uno de sus turnos y termina el efecto sobre sí mismo si tiene éxito. Después de [[lookup @duration.value activity=EGZ4bS4HpJkfNG9s]] minuto, tiene éxito automáticamente.</p>',
        "entries.mmAncientGreenDr.items.mmPoisonBreath00.description":
            '<p class="feature"><em>Tirada de salvación de Constitución:</em> CD [[lookup @save.dc.value activity=lnabW9bM51HoluPp]], cada criatura en un área de [[lookup @target.template.size activity=lnabW9bM51HoluPp]] pies con forma de [[lookup @target.template.type capitalize activity=lnabW9bM51HoluPp]].</p><p class="feature"><em>Fallo:</em> [[/damage average]] de daño.</p><p class="feature"><em>Éxito:</em> La mitad del daño.</p>',
        "entries.mmGreenDragonWyr.items.mmPoisonBreath00.description":
            '<p class="feature"><em>Tirada de salvación de Constitución:</em> CD [[lookup @save.dc.value activity=lnabW9bM51HoluPp]], cada criatura en un área de [[lookup @target.template.size activity=lnabW9bM51HoluPp]] pies con forma de [[lookup @target.template.type capitalize activity=lnabW9bM51HoluPp]].</p><p class="feature"><em>Fallo:</em> [[/damage average]] de daño.</p><p class="feature"><em>Éxito:</em> La mitad del daño.</p>',
        "entries.mmAnimalLord0000.items.mmLordlyPresence.effects.gZ5h0K8uFTRui7av.description":
            '<p>El objetivo queda confundido mágicamente hasta el final de su siguiente turno. Mientras está confundido, resta [[/r 1d4]] de sus tiradas de salvación.</p>',
        "entries.mmAnimalLord0000.items.mmAnimalSpirit00.effects.ERS5n6nHszCnoySl.description":
            '<p>El usuario tiene ventaja en las tiradas de ataque contra el objetivo hasta el comienzo del siguiente turno del usuario.</p>',
        "entries.mmOchreJelly0000.items.mmSplit000000000.activities.zoXFSgzmWq8frUjI.activation.condition":
            "es Grande o Mediana y tiene 10 puntos de golpe o más, queda malherida o recibe daño de relámpago o cortante.",
        "entries.mmPlanetar000000.items.fkctWMs3HtVhRarn.effects.RMeb9TUrFdhXMTzz.description":
            '<p>Durante la duración, los Celestiales, Elementales, Feéricos, Infernales y Muertos vivientes tienen desventaja en las tiradas de ataque contra ti. Puedes terminar el conjuro antes de tiempo usando una de las siguientes funciones especiales: <strong>Romper encantamiento</strong> o <strong>Expulsión</strong>.</p>',
        "entries.mmArchhag0000000.items.mmLegendaryResis.activities.nLPRJi7ipeAet7ir.activation.condition":
            "falla una tirada de salvación",
        "entries.mmAnimalLord0000.items.mmLordlyPresence.activities.54pvTrWlc7CB2ra6.name": "Asustado",
        "entries.mmPhaseSpider000.items.mmEtherealJaunt0.name": "Salto etéreo"
    },
    "features": {
        "entries.mmAnimalSpirit00.description": ANIMAL_SPIRIT,
        "entries.mmAnimalSpirit00.effects.ERS5n6nHszCnoySl.description":
            '<p>El usuario tiene ventaja en las tiradas de ataque contra el objetivo hasta el comienzo del siguiente turno del usuario.</p>',
        "entries.mmLordlyPresence.description": LORDLY_PRESENCE,
        "entries.mmLordlyPresence.effects.1JhQS3UFjWKSZqyP.description":
            '<p>El objetivo tiene la condición &amp;Reference[Charmed apply=false]{Hechizado} hasta el final de su siguiente turno. Mientras está hechizado, también tiene la condición &amp;Reference[Incapacitated apply=false]{Incapacitado}.</p>',
        "entries.mmLordlyPresence.effects.BR99gMLiBwIoLHVU.description":
            '<p>El objetivo tiene la condición &amp;Reference[Frightened apply=false]{Asustado} hasta el final de su siguiente turno.</p>',
        "entries.mmLordlyPresence.effects.gZ5h0K8uFTRui7av.description":
            '<p>El objetivo queda confundido mágicamente hasta el final de su siguiente turno. Mientras está confundido, resta [[/r 1d4]] de sus tiradas de salvación.</p>',
        "entries.mmLordlyPresence.activities.54pvTrWlc7CB2ra6.name": "Asustado",
        "entries.mmEtherealJaunt0.name": "Salto etéreo"
    }
}


def set_path(data: dict[str, Any], path: str, value: str) -> bool:
    target: Any = data
    parts = path.split(".")
    for part in parts[:-1]:
        target = target[part]
    changed = target.get(parts[-1]) != value
    target[parts[-1]] = value
    return changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    total = 0
    for pack, updates in UPDATES.items():
        path = COMPENDIUM / f"dnd-monster-manual.{pack}.json"
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        changes = sum(set_path(data, field, value) for field, value in updates.items())
        if args.write and changes:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{pack}: {changes} reviewed field(s) normalized")
        total += changes
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
