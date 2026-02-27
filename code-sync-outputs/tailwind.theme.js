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
            },
            "secondary": {
                  "50": "var(--color-brand-secondary-50)",
                  "100": "var(--color-brand-secondary-100)",
                  "200": "var(--color-brand-secondary-200)",
                  "300": "var(--color-brand-secondary-300)",
                  "400": "var(--color-brand-secondary-400)",
                  "500": "var(--color-brand-secondary-500)",
                  "600": "var(--color-brand-secondary-600)",
                  "700": "var(--color-brand-secondary-700)",
                  "800": "var(--color-brand-secondary-800)",
                  "900": "var(--color-brand-secondary-900)"
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
      },
      "status": {
            "success": {
                  "default": "var(--color-status-success-default)",
                  "subtle": "var(--color-status-success-subtle)",
                  "text": "var(--color-status-success-text)",
                  "border": "var(--color-status-success-border)"
            },
            "warning": {
                  "default": "var(--color-status-warning-default)",
                  "subtle": "var(--color-status-warning-subtle)",
                  "text": "var(--color-status-warning-text)",
                  "border": "var(--color-status-warning-border)"
            },
            "danger": {
                  "default": "var(--color-status-danger-default)",
                  "subtle": "var(--color-status-danger-subtle)",
                  "text": "var(--color-status-danger-text)",
                  "border": "var(--color-status-danger-border)"
            },
            "info": {
                  "default": "var(--color-status-info-default)",
                  "subtle": "var(--color-status-info-subtle)",
                  "text": "var(--color-status-info-text)",
                  "border": "var(--color-status-info-border)"
            }
      },
      "text": {
            "secondary": "var(--color-text-secondary)",
            "placeholder": "var(--color-text-placeholder)",
            "disabled": "var(--color-text-disabled)",
            "inverse": "var(--color-text-inverse)",
            "on-brand": "var(--color-text-on-brand)"
      },
      "background": {
            "secondary": "var(--color-background-secondary)",
            "disabled": "var(--color-background-disabled)",
            "overlay": "var(--color-background-overlay)"
      },
      "border": {
            "strong": "var(--color-border-strong)",
            "focus": "var(--color-border-focus)",
            "disabled": "var(--color-border-disabled)"
      },
      "icon": {
            "secondary": "var(--color-icon-secondary)",
            "disabled": "var(--color-icon-disabled)",
            "on-brand": "var(--color-icon-on-brand)"
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
      "7": "var(--spacing-7)",
      "8": "var(--spacing-8)",
      "9": "var(--spacing-9)",
      "10": "var(--spacing-10)",
      "11": "var(--spacing-11)",
      "12": "var(--spacing-12)"
},
      borderRadius: {
      "none": "var(--radius-none)",
      "sm": "var(--radius-sm)",
      "md": "var(--radius-md)",
      "lg": "var(--radius-lg)",
      "xl": "var(--radius-xl)",
      "2xl": "var(--radius-2xl)",
      "full": "var(--radius-full)"
},
      boxShadow: {
      "none": "var(--shadow-none)",
      "xs": "var(--shadow-xs)",
      "sm": "var(--shadow-sm)",
      "md": "var(--shadow-md)",
      "lg": "var(--shadow-lg)",
      "xl": "var(--shadow-xl)",
      "2xl": "var(--shadow-2xl)"
},
      fontFamily: {
      "sans": "var(--font-family-sans)",
      "display": "var(--font-family-display)",
      "ui": "var(--font-family-ui)"
},
      fontSize: {
      "lg": "var(--font-size-lg)",
      "2xl": "var(--font-size-2xl)",
      "4xl": "var(--font-size-4xl)"
}
    }
  }
}
