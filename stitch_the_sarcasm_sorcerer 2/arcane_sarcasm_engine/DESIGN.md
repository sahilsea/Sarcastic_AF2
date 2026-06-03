---
name: Arcane Sarcasm Engine
colors:
  surface: '#171305'
  surface-dim: '#171305'
  surface-bright: '#3e3926'
  surface-container-lowest: '#110e02'
  surface-container-low: '#1f1c0b'
  surface-container: '#23200f'
  surface-container-high: '#2e2a18'
  surface-container-highest: '#393522'
  on-surface: '#ebe2c8'
  on-surface-variant: '#c1c8c3'
  inverse-surface: '#ebe2c8'
  inverse-on-surface: '#35301e'
  outline: '#8b928e'
  outline-variant: '#414845'
  surface-tint: '#adcec0'
  primary: '#adcec0'
  on-primary: '#19362c'
  primary-container: '#0d2b22'
  on-primary-container: '#759487'
  inverse-primary: '#476459'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#ddb7ff'
  on-tertiary: '#4a0080'
  tertiary-container: '#3b0068'
  on-tertiary-container: '#ad72e6'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#c9eadc'
  primary-fixed-dim: '#adcec0'
  on-primary-fixed: '#022018'
  on-primary-fixed-variant: '#2f4c42'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#f0dbff'
  tertiary-fixed-dim: '#ddb7ff'
  on-tertiary-fixed: '#2c0050'
  on-tertiary-fixed-variant: '#622599'
  background: '#171305'
  on-background: '#ebe2c8'
  surface-variant: '#393522'
typography:
  display-lg:
    fontFamily: Libre Caslon Text
    fontSize: 56px
    fontWeight: '700'
    lineHeight: 64px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Libre Caslon Text
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Libre Caslon Text
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-md:
    fontFamily: EB Garamond
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  label-sm:
    fontFamily: EB Garamond
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  margin-page: 2rem
  gutter-grid: 1.5rem
  stack-sm: 0.75rem
  stack-md: 1.5rem
  stack-lg: 3rem
---

## Brand & Style

The visual identity of this design system is rooted in **Mystical Scholarship**. It is designed to evoke the feeling of uncovering hidden truths within ancient manuscripts, blending the wonder of the Wizarding World with the precision of modern linguistics. The target audience seeks a sophisticated, "magical" experience that feels more like an enchantment than a data calculation.

The style is a hybrid of **Tactile/Skeuomorphic** and **Glassmorphism**. We utilize rich, organic textures like aged parchment and cold stone, layered with ethereal "soul-fire" glows and translucent magical fields. The interface should feel like a living artifact—vibrant, atmospheric, and slightly mysterious.

## Colors

The palette is dominated by **Forbidden Forest Green** and **Aged Parchment**.

- **Primary (Emerald Deep):** A dark, atmospheric green used for the vast background and structural foundations, inspired by the deep shadows of Hogwarts' grounds.
- **Secondary (Enchanted Gold):** Used sparingly for interactive elements, highlights, and "divination" results to signify premium quality and ancient value.
- **Neutral (Vellum):** A warm, off-white used for text and parchment surfaces to ensure readability without the harshness of pure white.
- **Sarcasm Indicator Scale:** A spectrum ranging from **Emerald** (Truthful/Low Sarcasm) to **Mystical Purple/Crimson** (High Sarcasm), utilizing a "glow" effect to indicate the intensity of the magical detection.

## Typography

The typography system follows a **Scholarly Serif** hierarchy.

- **Headlines:** Use **Libre Caslon Text** for an authoritative, editorial feel that mimics high-end wizarding publications.
- **Body:** Use **EB Garamond** for all long-form content. The high x-height and classical proportions make it ideal for the "scroll" aesthetic while remaining highly legible.
- **Labels:** Small labels and UI metadata use a slightly tracked-out, semi-bold weight of EB Garamond or a similar classical Roman serif to maintain the "etched in stone" or "inked on vellum" appearance.

## Layout & Spacing

This design system employs a **Fixed Center-Column Grid** for desktop to mimic the focused nature of reading a single tome. 

- **The Layout:** A 12-column grid with wide outer margins (resembling page gutters). Content is often housed in "parchment blocks" that do not span the full width of the screen, creating a sense of intimacy.
- **Rhythm:** Spacing is generous, utilizing a 8px (0.5rem) base unit. We favor vertical stacking to simulate the flow of a scroll.
- **Mobile Adaptivity:** On mobile, margins shrink to 16px and the parchment containers become edge-to-edge with a subtle inner shadow to maintain depth.

## Elevation & Depth

Hierarchy is established through **Material Contrast** rather than traditional drop shadows.

1.  **Level 0 (The Void):** The dark green, atmospheric background.
2.  **Level 1 (Parchment):** Interactive surfaces and content blocks use a parchment texture with "deckled edges" (irregular borders).
3.  **Level 2 (Ethereal Glow):** High-priority items or sarcasm detections do not "lift" off the page; instead, they emit a soft, inner and outer neon-like glow in their respective sarcasm color.
4.  **Overlays:** Modals and tooltips use a "Frosted Black-Quartz" glass effect—dark, semi-transparent, and heavily blurred—as if looking through a dark scrying mirror.

## Shapes

The shape language is **Organic and Traditional**. 

While we use a "Soft" (0.25rem) setting for standard buttons and inputs, primary containers (parchment blocks) should utilize **irregular border-radii** or SVG masks to simulate the look of hand-cut paper or aged vellum. Hard geometric perfection should be avoided to maintain the "hand-crafted" magical feel.

## Components

- **The "Scribe" Input:** Text areas for user input are styled like blank scrolls. They feature a subtle "lined paper" background and an animated quill cursor.
- **Divination Buttons:** Primary buttons are Gold-bordered with a "shimmer" hover effect. Secondary buttons use a simple gold outline (ghost style).
- **The Sarcasm Meter:** A circular gauge resembling an astrolabe or an ancient compass. The needle moves with a slight "jitter" to simulate mechanical/magical calculation.
- **Incantation Chips:** Used for sarcasm tags (e.g., "Irony," "Satire"). These look like wax seals or small leather tags tied to the content.
- **Parchment Cards:** Content containers feature a subtle noise texture and a very thin, 1px gold border to separate them from the dark forest background.