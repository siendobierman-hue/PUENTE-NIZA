# Puente Niza · Realidad Aumentada

Esta carpeta es la experiencia AR lista para publicar. Funciona en Android y en iPhone/iPad, sin instalar ninguna app.

| Archivo | Uso |
|---|---|
| index.html | Página con visor 3D, selector "Con entorno / Solo estructura" y botón AR |
| puente_entorno.glb / .usdz | Puente + terreno con ortofoto + árboles, maqueta 1:400 (≈1,0 × 0,5 m) |
| puente_estructura.glb / .usdz | Solo el puente, rampas, vehículos y luminarias, maqueta 1:150 (≈1,9 × 0,65 m) |
| model-viewer.min.js | Librería del visor (incluida, no depende de internet externo) |
| crear_qr.py | Genera el código QR cuando ya tengas la URL pública |

## Publicar gratis con GitHub Pages

1. Crea un repositorio público en github.com, por ejemplo `puente-niza`.
2. **Add file → Upload files** y arrastra TODOS los archivos de esta carpeta. Luego, **Commit changes**.
3. **Settings → Pages → Branch: main / (root) → Save**.
4. En 1–2 minutos queda en: `https://TU_USUARIO.github.io/puente-niza/`

## Crear el QR

```
pip install "qrcode[pil]"
python3 crear_qr.py https://TU_USUARIO.github.io/puente-niza/
```

Imprime `qr_puente_niza.png`. Al escanearlo se abre el visor; con **"Ver en tu espacio (AR)"** se coloca la maqueta sobre el piso o una mesa, y se puede pellizcar para agrandarla.

## Notas

- El modelo original (838.000 triángulos, terreno de 1,2 km y ortofoto de 17 MB) se optimizó para el celular: recorte de unos 400 × 210 m alrededor del puente, textura de 4096 px (2048 px en iPhone), en total 9 MB para la versión con entorno.
- La versión "Solo estructura" (3,9 MB) carga más rápido con datos móviles.
