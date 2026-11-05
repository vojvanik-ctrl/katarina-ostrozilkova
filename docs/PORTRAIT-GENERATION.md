# FMK gallery portrait

Source: the author's actual photograph, `assets/cv-portrait.webp`.

Method: built-in imagegen, identity-preserving style transfer. The original photograph and the website's separate illustrated hero portrait were preserved. The result is used only through `photoStamp` in `portfolio.json`.

Output: `assets/fmk/portrait-stamp.png`, PNG RGBA, 1122 × 1402 px, real alpha values from 0 to 255. The generator returned an aspect ratio very close to 4:5 rather than the exact requested 1200 × 1500 px. No rescaling or cropping was applied afterwards. Eye placement and head scale are visual approximations, not measured guarantees.

## Generation prompt

Use case: style-transfer, identity-preserve.
Asset type: a finished transparent PNG portrait for the FMK student portfolio gallery, based only on the supplied actual photograph of Katarína.
Primary request: turn the same woman from the input photograph into a detailed multicolour rubber-stamp print portrait or fine printmaking illustration. Preserve her identity, age, natural facial proportions, expression, head direction, hair, eyeglasses, the shape and cut of the white collared shirt. No beautification, slimming, caricature or invented face. Use her original photo, not any other face.
Composition: one person, head, shoulders and upper chest, upright 4:5 canvas, target 1200 by 1500 pixels. Keep all of her head and hair. Leave 6 to 9 percent canvas height above her head. Crown-to-chin occupies 45 to 50 percent of image height; eyes near 30 to 35 percent from top. Face centred horizontally. Respect the original slightly turned pose. Do not stretch anatomy.
Style: detailed authentic ink print with irregular ink edges, small gaps in ink and fine print grain; eyes, nose and mouth remain readable and recognisable. Restricted palette of charcoal black, muted brick red, dark slate blue and forest green. Convert clothing into this palette while preserving its form and cut. No watercolour, comic, smooth plastic AI finish or paper rectangle.
Background: genuinely transparent alpha. Very sparse abstract ink traces or subtle leaves near the shoulders only. No scenery, landmarks, flags, frame, folder shape, text, name, labels, number, logo or shadow. No checkerboard painted into the image. The ink portrait should sit directly on the gallery paper later.
Output: one portrait PNG with actual transparent background and exact 4:5 aspect ratio.
