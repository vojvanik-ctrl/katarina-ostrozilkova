# Portfolio update, 23 October 2026

The updated brief is DESIGN – kópia, modified on 23 October 2026. Its Extras section calls for a retro TV power-on, a paused-film menu, a botanical setting dominated by leaves, navigation on the left, and previous/next controls that seek during playback. The supplied portrait is introduced on the home page. On widths up to 900 px, all television hardware moves beneath the screen; dial numbers are removed.

## Artwork

Created with the built-in image generation tool. Original project images and CV remain the supplied materials. The portrait is a stylized interpretation of the supplied photo.

- Portrait used by the website: `dist/assets/portrait.webp`
- Botanical background used by the website: `dist/assets/leaves.webp`

Portrait prompt:

> Use case: identity-preserve and style-transfer. Create a finished standalone portrait asset for Katarína's personal portfolio website. Image 1 is the EDIT TARGET, the actual young woman from the supplied photograph. Preserve her recognizable facial structure and proportions, brown shoulder-length hair parted as shown, round thin-rim glasses, warm natural smile, small forehead marks, and white collared shirt. Keep her age and identity. Repaint as a restrained hand-drawn traditional 2D animation portrait, clean fine pencil/ink contours, flat cel color with soft restrained gouache shadows, natural anatomy and realistic eyes. Supporting images 2 and 3 are STYLE REFERENCES ONLY for hand-painted botanical children's animation atmosphere and muted forest light; DO NOT reproduce any characters, insects, logos, text, or scene from them. Chest-up three-quarter portrait with the same head pose and camera gaze as photo, entire hair and shoulders inside image, softly warm light from upper left, subtle moss-green reflected light in shadows. Her white shirt is warm ivory. Transparent background, no scenery, no frame, no badge, no text, no decorative leaves overlapping her face. A quiet recognizable human portrait rather than a generic cute anime face. Professional enough for a personal portfolio, handmade and nostalgic. Portrait canvas, transparent background.

Background prompt:

> Use case: illustration-story. Asset type: wide landscape botanical background for a retro television website menu. Generate an original painterly view from beneath enormous familiar woodland leaves. Reference images show the desired traditional hand-painted animation BACKGROUND qualities only. Do NOT reproduce characters or copyrighted lettering or movie compositions. Focus completely on nature, most importantly big leaves. Imagine the camera very low on a mossy forest floor under a canopy of broad heart-shaped burdock and ivy leaves with visible delicate veins, a few round dew drops, twisting natural stems, moss and soft shadows. Foreground leaves at top left and right edges, layered emerald, bottle-green and olive foliage, warm lime light filtering through translucent leaves toward upper right, soft distant deep teal and dark forest green. Hand-painted gouache washes on paper with finely inked edges, charming imperfect outlines, rich saturated but natural colors, nostalgic European and Japanese 2D children's animation backgrounds, atmospheric and slightly mysterious. Not photographic, not 3D, no glossy plastic, no fantasy castle, no stream, no small flowers. Left 35 percent quiet and dark enough for cream-colored menu text, central lower region quiet green for portrait overlay, right foliage luminous and expressive. Background only, no people, no faces, no insects, no animals, no typography, no logos, no UI. 16:9 composition.

## Verification

- JavaScript syntax, unique static DOM IDs, and referenced local assets checked.
- Desktop home, project navigation, power off/on and playback preview checked in the browser.
- Mobile widths 320 px and 390 px: no horizontal page overflow, all hardware below the picture, each hardware button at least 44 by 44 px.
- Raiders Entertainment detail checked at both mobile widths, including loaded artwork and a route back to the portfolio.
- The Animation section remains explicitly labelled as a preview because no animation video was supplied.


## Text CV, continuous movement and sound sketches

The CV is selectable semantic HTML translated into English from the two supplied screenshots. It includes all five jobs, all three creative projects, technical skills, both languages, both education entries, and both email addresses. No CV image is rendered.

A persistent clipped background layer pans gently over 24 seconds in each direction. It stays behind the UI through page changes, pauses when the TV is off or the page is hidden, and respects reduced-motion preferences. A motion pause control is available in the Soundtrack panel.

Three original 32-second synthesized audio sketches are available through Music: Forest air (airy ambient pads), Storybook (music box), and Late broadcast (warm synth chords). Sound starts off, begins only after a visitor interaction, loops across navigation and pauses with the TV or hidden tab. The volume knob switches the music on or off. All audio files are local; no streaming service or third-party music is used. The source is in `scripts/generate-soundtracks.py`.

Checked selectable text and complete CV content, JavaScript syntax, local assets, desktop playback of all three tracks, mobile playback, volume off, power-off pause, and mobile widths 320 and 390 px. A focus-induced shift of the mobile header was fixed by clipping the moving layer inside a dedicated wrapper; the screen remains at scrollTop 0 after mobile CV navigation.


## Small visual adjustments

Background movement now takes 24 seconds in each direction, twice the previous speed. The original supplied photograph appears alongside the text CV, with a smaller responsive layout on phones. A small yellow handwritten “Do not touch” sticky note and curved arrow sit below the Power button. The note is decorative and never intercepts clicks. Its Caveat font is hosted locally with the included OFL licence.


## Simplified mobile controls

At widths up to 900 px, the bottom panel now contains only Previous, Next and the music on/off dial. The dial has a visible Music label beneath it. The channel dial, Power button and handwritten note are hidden on mobile. The desktop television keeps its existing controls.

## FMK profile and portable export

The buildless site now includes the exact FMK `portfolio.json` schema. Shared name, study programme and CV photograph are read from this file, with an automatically generated inline snapshot for offline fallback. The longer English introduction and CV remain separate content. The profile uses the explicitly confirmed SK code and a 105-character Czech bio. Its public portfolio URL is pending until the standalone site is publicly hosted. A separate transparent print-style portrait is available for the gallery without changing the existing hero or CV image. The standalone GitHub export places index.html and portfolio.json at its root and includes all local assets, documentation, a .nojekyll marker and profile maintenance scripts.
