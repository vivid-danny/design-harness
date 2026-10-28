/**
 * Primitive color families (gray, blue, magenta, etc.) live in
 * primitive-colors/tokens.grouped.ts, synced from Figma via the Token Manager —
 * see build-scripts/sync-tokens.ts. This file is hand-maintained: it merges
 * in the alpha-scale families not sourced from Figma (white, dark).
 */
import primitiveColors from '../primitive-colors/tokens.grouped'

type ColorShades = {
    [key: string]: string
}

type Colors = {
    gray: ColorShades
    white: ColorShades
    dark: ColorShades
    blue: ColorShades
    cobalt: ColorShades
    green: ColorShades
    indigo: ColorShades
    lime: ColorShades
    orange: ColorShades
    red: ColorShades
    yellow: ColorShades
    magenta: ColorShades
    teal: ColorShades
}

export type BrandColors = {
    primary: ColorShades
    secondary: ColorShades
}

type PrimitiveColorKey = keyof Omit<Colors, 'white' | 'dark'>

// Declared as a Record rather than an array so the compiler enforces
// exhaustiveness: adding a palette to Colors without listing it here fails to
// build, instead of leaving a key that the type claims exists but is undefined
// at runtime. Palettes Figma publishes but Colors doesn't declare (amber,
// blueGrey, cyan, lightGreen, …) are excluded by omission.
const PRIMITIVE_FAMILIES: Record<PrimitiveColorKey, true> = {
    gray: true,
    blue: true,
    cobalt: true,
    green: true,
    indigo: true,
    lime: true,
    orange: true,
    red: true,
    yellow: true,
    magenta: true,
    teal: true,
}

// The generated palettes are typed loosely (Record<string, string | number |
// boolean>) and carry members that aren't part of a shade scale — gray ships a
// `white` and a `black`. Validate rather than cast: a bad sync should break the
// build with a pointed message, not surface as an undefined color deep in a
// component.
const toShadeScale = (family: string, palette: Record<string, string | number | boolean> | undefined) => {
    if (!palette) {
        throw new Error(`Primitive color family "${family}" is missing from the generated tokens.`)
    }

    const shades: ColorShades = {}
    for (const [shade, value] of Object.entries(palette)) {
        if (!/^\d+$/.test(shade)) continue
        if (typeof value !== 'string') {
            throw new Error(`Primitive color ${family}.${shade} is a ${typeof value}, expected a string.`)
        }
        shades[shade] = value
    }

    if (Object.keys(shades).length === 0) {
        throw new Error(`Primitive color family "${family}" has no numeric shades in the generated tokens.`)
    }

    return shades
}

const primitives = {} as Record<PrimitiveColorKey, ColorShades>
for (const family of Object.keys(PRIMITIVE_FAMILIES) as PrimitiveColorKey[]) {
    primitives[family] = toShadeScale(family, primitiveColors[family])
}

const colors: Colors = {
    ...primitives,
    white: {
        '10': '#FFFFFF19',
        '20': '#FFFFFF33',
        '30': '#FFFFFF4C',
        '40': '#FFFFFF66',
        '50': '#FFFFFF7F',
        '100': '#FFFFFFFF',
    },
    dark: {
        '10': '#04092C19',
        '20': '#04092C33',
        '30': '#04092C4C',
        '40': '#04092C66',
        '50': '#04092C7F',
    },
}

export default colors
