/** @type {import('tailwindcss').Config} */
module.exports = {
  theme: {
    extend: {
      colors: {
      "brand": {
            "primary": {
                  "50": "var(--color-brand-primary-50)",
                  "100": "var(--color-brand-primary-100)",
                  "200": "var(--color-brand-primary-200)",
                  "300": "var(--color-brand-primary-300)",
                  "400": "var(--color-brand-primary-400)",
                  "500": "var(--color-brand-primary-500)",
                  "600": "var(--color-brand-primary-600)",
                  "700": "var(--color-brand-primary-700)",
                  "800": "var(--color-brand-primary-800)",
                  "900": "var(--color-brand-primary-900)"
            }
      },
      "neutral": {
            "50": "var(--color-neutral-50)",
            "100": "var(--color-neutral-100)",
            "200": "var(--color-neutral-200)",
            "300": "var(--color-neutral-300)",
            "400": "var(--color-neutral-400)",
            "500": "var(--color-neutral-500)",
            "600": "var(--color-neutral-600)",
            "700": "var(--color-neutral-700)",
            "800": "var(--color-neutral-800)",
            "900": "var(--color-neutral-900)"
      }
},
      spacing: {
      "0": "var(--spacing-0)",
      "1": "var(--spacing-1)",
      "2": "var(--spacing-2)",
      "3": "var(--spacing-3)",
      "4": "var(--spacing-4)",
      "5": "var(--spacing-5)",
      "6": "var(--spacing-6)",
      "8": "var(--spacing-8)",
      "10": "var(--spacing-10)",
      "12": "var(--spacing-12)"
},
      borderRadius: {
      "none": "var(--radius-none)",
      "sm": "var(--radius-sm)",
      "md": "var(--radius-md)",
      "lg": "var(--radius-lg)",
      "xl": "var(--radius-xl)",
      "full": "var(--radius-full)"
},
      boxShadow: {
      "sm": "var(--shadow-sm)",
      "md": "var(--shadow-md)"
},
      fontFamily: {
      "base": "var(--font-family-base)"
},
      fontSize: {
      "sm": "var(--font-size-sm)",
      "base": "var(--font-size-base)",
      "lg": "var(--font-size-lg)",
      "xl": "var(--font-size-xl)"
}
    }
  }
}
