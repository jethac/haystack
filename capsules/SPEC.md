# Capsule art spec — Find the Original

Store "small capsule" art for a parody storefront. Each file is the search-results thumbnail for one fake game that is cashing in on a viral "needle in a haystack" game.

The real game's capsule (`original.jpg`, not generated) is: blue sky with white clouds, a round golden haystack dome at the bottom, cream condensed display type reading NEEDLE IN A HAYSTACK SIMULATOR. The clones below are all trying to be that game, but **each clone was made by a different cheap studio, so each one must look clearly different from the others**: different medium, palette, typeface, composition and camera. Diversity across the set matters more than polish.

## Output

- One PNG per id, saved as `<id>.png` in this folder, exactly **462 × 174** px.
- Generate wide (landscape), then center-crop to 462:174 and resize to 462 × 174 with Python PIL (`Image.LANCZOS`). Keep the whole title inside the crop.
- Skip any id whose PNG already exists.

## Rules (Steamworks graphical asset rules, followed as if these were real Steam capsules)

- The capsule contains **only**: game artwork, the game name, and the official subtitle if one is listed. Nothing else.
- **No** stickers, badges, banners or ribbons ("ORIGINAL", "NEW", "SALE", "DEMO" badges, etc.), review scores, award laurels, quotes, discount copy, URLs, platform icons, studio logos, or any other text.
- The title must nearly fill the capsule and stay readable when shrunk to 184 × 69.
- PG-13. No real brands, no real people, no copying the real capsule's exact art.
- Render the title text **exactly** as written, letter for letter, including odd spellings (`ln`, `SimuIator`, `Simulater`, `Neeedle`). They are deliberate; do not correct them.

## The capsules

| id | title text | subtitle | style (each one different) |
| --- | --- | --- | --- |
| lowercase-l | Needle ln A Haystack Simulator | — | A close knockoff of the real one: blue sky, clouds, haystack dome, cream condensed type, but slightly worse, flatter clip-art haystack. |
| capital-i | Needle In A Haystack SimuIator | — | Glossy low-poly 3D render, teal sky, chunky beveled gold 3D title. |
| sim-demo | Needle In A Haystack Simulator Demo | — | 16-bit pixel art, SNES palette, pixel font title. |
| sim-tm | Needle In A Haystack Simulator™ | — | Premium corporate AAA key art: moody photoreal golden-hour haystack, thin silver serif title. |
| sim-2 | Needle In A Haystack Simulator 2 | — | Action sequel energy: explosions of hay, lens flares, metallic chrome title with a huge "2". |
| sim-original | Needle In A Haystack Simulator (Original) | — | Another near-knockoff of the real one, but at night: dark blue sky, stars, moonlit haystack dome, cream condensed type. |
| simulater | Needle In A Haystack Simulater | — | Obvious asset-flip: stock-photo haystack, MS-Paint-looking rainbow WordArt title. |
| the-haystack | Needle In The Haystack Simulator | — | Anime key visual: girl in a straw hat looking at a haystack, pastel sky, cute rounded title. |
| hay-stack | Needle In A Hay Stack Simulator | — | Claymation / stop-motion look, plasticine haystack, lumpy clay letters. |
| the-original | Needle In A Haystack Simulator | The Original | Knockoff of the real one in sepia/"vintage film" treatment, grainy, cream condensed type. |
| neeedle | Neeedle In A Haystack Simulator | — | Vaporwave: pink/purple grid, marble bust made of hay, chrome gradient title. |
| sim-vr | Needle In A Haystack Simulator VR | — | Sci-fi neon: cyan wireframe haystack on black, glowing HUD-style title. |
| sim-sim | Needle In A Haystack Simulator Simulator | — | Office-sim look: a desk with a monitor showing a haystack, beige corporate palette, clean sans title. |
| dlc | Haystack Simulator | Needle DLC | Watercolor children's-book illustration of a haystack, hand-lettered title. |
| plain | Needle In A Haystack | — | Bright cartoon: yellow sunburst, a kid in red overalls with a pitchfork, bubbly white title with black outline. |
| plain-demo | Needle In A Haystack Demo | — | Same studio as `plain`: same cartoon kid and bubbly title, slightly different pose. |
| barn | The Needle In The Haystack | — | Red barn wall, white trim, western slab-serif title. |
| queen | A Needle In A Haystack | The Queen's Needle | Medieval painted fantasy: sunset castle, hay bales, gold blackletter title. |
| story | Story of The Needle | — | Moody narrative indie: dusk farm, lone farmer silhouette, big moon, thin elegant serif title. |
| coop-hunt | Needle Hunt | A Haystack Challenge | Loud party-game: orange and purple, cartoon hands grabbing hay, bouncy sticker-free bubble title. |
| sheep | Needle In A Haystack | A Time For Sheep | Photoreal hay close-up, a sheep, title in a black box with white condensed type. |
| sorting | A Needle In A Haystack | Sorting Simulator | Cozy isometric barn interior with crates of hay, rounded orange title. |
| billion | Needle In A Billion Haystacks | — | Epic wide field of countless haystacks to the horizon, tiny person and goat, big white comic title with blue outline. |
| goat | Needle In A Haystack | Goat Edition | Chaotic physics-game energy: a goat mid-air crashing into hay, ragdoll vibe, scratchy hand-drawn title. |
| find | Find The Needle | Simulator | Factory automation: conveyor belts moving hay through machines, industrial yellow/black title. |
| hay-five | Hay! Five Million! | — | Hyper-casual mobile ad look: hot pink background, exploding hay, huge bouncy title. |
| tycoon | Needle In A Haystack Tycoon | — | Early-2000s PC tycoon box-art: top-down farm, gold coins, embossed gold title. |
| royale | Needle In A Haystack | Battle Royale | Shooter key-art parody: three cartoon farmers posing with pitchforks, hay-coloured storm circle, aggressive italic title. |
| idle | Needle In A Haystack Idle | — | Flat cute mobile idle game, smiling haystack character, pastel mint background. |
| needlestack | Needle In A Needlestack | — | Horror: dark red and black, a heap of silver sewing needles, one straw of hay, dripping horror title. |
