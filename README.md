# __name__

Deze kleine repository is een experiment om de werking van `__name__` te verduidelijken.

Voer deze code uit en verklaar de output:

    python a.py
    python b.py

# Extra

`sys.modules` geeft een overzicht van alle geladen modules.
Met `len(sys.modules`) kunnen we dus opvragen hoeveel modules geladen zijn.

Doe volgend experiment:

1. Controleer de lengte van `sys.modules` in de Python-interpreter:

- start `python`
- importeer de `sys`-module: `import sys`
- optioneel: controleer de inhoud van `sys.modules`
- controleer de lengte van `sys.modules` met `len(sys.modules)`

2. Controleer de lengte van `sys.modules` in de **inspect interactively**-modus v.d. Python-interpreter

- start `python -i a.py`
- importeer de `sys`-module: `import sys`
- optioneel: controleer de inhoud van `sys.modules`
- controleer de lengte van `sys.modules` met `len(sys.modules)`

Je zou moeten zien dat er 1 extra module is geïmporteerd, nl. `a`.
