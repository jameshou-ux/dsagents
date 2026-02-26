const pptxgen = require("pptxgenjs");

let pres = new pptxgen();
pres.layout = 'LAYOUT_16x9';

const COLORS = {
    bg: "0B0B1A",          // Deep dark navy
    cyan: "00FFFF",
    magenta: "FF007F",
    purple: "6A0DAD",
    textTitle: "FFFFFF",
    textBody: "E2E8F0"     // Light gray-blue
};

function addGlassBackground(slide) {
    slide.background = { color: COLORS.bg };

    // Blurred colorful orbs (simulated via overlapping transparent OVALs)
    slide.addShape(pres.shapes.OVAL, {
        x: -1, y: -2, w: 6, h: 6, fill: { color: COLORS.purple, transparency: 60 }
    });
    slide.addShape(pres.shapes.OVAL, {
        x: 6, y: -1, w: 5, h: 5, fill: { color: COLORS.cyan, transparency: 75 }
    });
    slide.addShape(pres.shapes.OVAL, {
        x: -2, y: 3, w: 5, h: 5, fill: { color: COLORS.magenta, transparency: 80 }
    });
    slide.addShape(pres.shapes.OVAL, {
        x: 7, y: 3, w: 4, h: 4, fill: { color: COLORS.purple, transparency: 70 }
    });
}

function addGlassCard(slide, x, y, w, h) {
    // Create a RECTANGLE (avoid rounded to allow clean border) simulating frosted glass
    const makeShadow = () => ({ type: "outer", color: "000000", blur: 10, offset: 3, angle: 90, opacity: 0.3 });

    // Fill
    slide.addShape(pres.shapes.RECTANGLE, {
        x: x, y: y, w: w, h: h,
        fill: { color: "FFFFFF", transparency: 90 },
        line: { color: "FFFFFF", width: 0.5, transparency: 60 },
        shadow: makeShadow()
    });
}

// SLIDE 1: Title Slide
let s1 = pres.addSlide();
addGlassBackground(s1);

addGlassCard(s1, 1, 1.5, 8, 2.5);
s1.addText("The Emerald Suite Escape", {
    x: 1, y: 1.8, w: 8, h: 1,
    fontSize: 44, bold: true, color: COLORS.textTitle, align: "center", fontFace: "Outfit"
});
s1.addText("A historic 1920s lodge nestled on the shores of Mississagagon Lake.", {
    x: 1.5, y: 2.8, w: 7, h: 0.8,
    fontSize: 18, color: COLORS.textBody, align: "center", fontFace: "Outfit"
});

// SLIDE 2: The Hook & Location
let s2 = pres.addSlide();
addGlassBackground(s2);

addGlassCard(s2, 0.5, 0.5, 9, 1);
s2.addText("Your North Frontenac Sanctuary", {
    x: 1, y: 0.5, w: 8, h: 1,
    fontSize: 32, bold: true, color: COLORS.textTitle, align: "left", fontFace: "Outfit"
});

addGlassCard(s2, 0.5, 2, 4.25, 3);
addGlassCard(s2, 5.25, 2, 4.25, 3);

s2.addText([
    { text: "Located in peaceful Cloyne, Ontario.", options: { breakLine: true, bullet: true } },
    { text: "Within a family resort with direct beachfront access.", options: { breakLine: true, bullet: true } },
    { text: "Only 20 minutes to iconic Bon Echo Provincial Park.", options: { bullet: true } }
], {
    x: 0.8, y: 2.2, w: 3.8, h: 2,
    fontSize: 18, color: COLORS.textTitle, fontFace: "Outfit"
});

s2.addText("Map Point Placeholder / Scenic Aerial Image\n(Imagine Lake Mississagagon visible here)", {
    x: 5.4, y: 3, w: 4, h: 1,
    fontSize: 16, color: COLORS.textBody, align: "center", italic: true, fontFace: "Outfit"
});


// SLIDE 3: Suite Highlights
let s3 = pres.addSlide();
addGlassBackground(s3);

addGlassCard(s3, 0.5, 0.5, 9, 1);
s3.addText("Cozy, Character-Rich Comfort", {
    x: 1, y: 0.5, w: 8, h: 1,
    fontSize: 32, bold: true, color: COLORS.textTitle, align: "left", fontFace: "Outfit"
});

addGlassCard(s3, 0.5, 2, 9, 3);
s3.addText([
    { text: "Intimate Space:", options: { bold: true, breakLine: true } },
    { text: "Studio efficiency suite perfect for up to 2 guests.\n", options: { breakLine: true } },
    { text: "Modern Meets History:", options: { bold: true, breakLine: true } },
    { text: "1920s character paired with modern comforts (Wifi, Netflix, extremely comfortable bed).\n", options: { breakLine: true } },
    { text: "Romance Ready:", options: { bold: true, breakLine: true } },
    { text: "Ask about add-on adventure packages for couples.", options: { breakLine: true } }
], {
    x: 1, y: 2.2, w: 8, h: 2.5,
    fontSize: 18, color: COLORS.textTitle, fontFace: "Outfit"
});

// SLIDE 4: Four Seasons
let s4 = pres.addSlide();
addGlassBackground(s4);

addGlassCard(s4, 0.5, 0.5, 9, 1);
s4.addText("Adventure Awaits, All Year Round", {
    x: 1, y: 0.5, w: 8, h: 1,
    fontSize: 32, bold: true, color: COLORS.textTitle, align: "left", fontFace: "Outfit"
});

// Summer Column
addGlassCard(s4, 0.5, 2, 4.25, 3);
s4.addText("Summer Highlights", {
    x: 0.5, y: 2.2, w: 4.25, h: 0.5,
    fontSize: 22, bold: true, color: COLORS.cyan, align: "center", fontFace: "Outfit"
});
s4.addText([
    { text: "Swimming & beach access", options: { breakLine: true, bullet: true } },
    { text: "Canoe and kayak rentals", options: { breakLine: true, bullet: true } },
    { text: "Horseshoe pits", options: { breakLine: true, bullet: true } },
    { text: "Beach volleyball", options: { bullet: true } }
], {
    x: 0.8, y: 3, w: 3.8, h: 1.5,
    fontSize: 16, color: COLORS.textTitle, fontFace: "Outfit"
});

// Winter Column
addGlassCard(s4, 5.25, 2, 4.25, 3);
s4.addText("Winter Highlights", {
    x: 5.25, y: 2.2, w: 4.25, h: 0.5,
    fontSize: 22, bold: true, color: COLORS.magenta, align: "center", fontFace: "Outfit"
});
s4.addText([
    { text: "'Winter Wonderland' feel", options: { breakLine: true, bullet: true } },
    { text: "Indoor fireplace warmth", options: { breakLine: true, bullet: true } },
    { text: "Snowshoeing trails", options: { breakLine: true, bullet: true } },
    { text: "Ice fishing", options: { bullet: true } }
], {
    x: 5.55, y: 3, w: 3.8, h: 1.5,
    fontSize: 16, color: COLORS.textTitle, fontFace: "Outfit"
});

// SLIDE 5: Social Proof
let s5 = pres.addSlide();
addGlassBackground(s5);

addGlassCard(s5, 0.5, 0.5, 9, 1);
s5.addText("Rated Top 10% on Airbnb", {
    x: 1, y: 0.5, w: 8, h: 1,
    fontSize: 32, bold: true, color: COLORS.textTitle, align: "left", fontFace: "Outfit"
});

addGlassCard(s5, 0.5, 2, 9, 3);

// Large stat in center
s5.addText("4.84 / 5", {
    x: 0.5, y: 2.2, w: 4, h: 1.5,
    fontSize: 48, bold: true, color: COLORS.cyan, align: "center", fontFace: "Outfit"
});
s5.addText("Overall Rating (309 Reviews)\n★ ★ ★ ★ ★", {
    x: 0.5, y: 3.6, w: 4, h: 1,
    fontSize: 18, color: COLORS.textTitle, align: "center", fontFace: "Outfit"
});

s5.addText([
    { text: "\"Seamless Private Entry\"", options: { italic: true, breakLine: true } },
    { text: "- Check-in Review\n", options: { color: COLORS.textBody, fontSize: 14, breakLine: true } },
    { text: "\"Extremely Responsive Superhost\"", options: { italic: true, breakLine: true } },
    { text: "- Communication Review\n", options: { color: COLORS.textBody, fontSize: 14, breakLine: true } },
    { text: "\"One of our best Airbnb experiences.\"", options: { italic: true, breakLine: true } },
    { text: "- Overall Value Review", options: { color: COLORS.textBody, fontSize: 14 } }
], {
    x: 5, y: 2.5, w: 4, h: 2,
    fontSize: 18, color: COLORS.textTitle, fontFace: "Outfit"
});

// SLIDE 6: Call To Action
let s6 = pres.addSlide();
addGlassBackground(s6);

addGlassCard(s6, 2, 1.5, 6, 2.5);
s6.addText("Unwind at the Emerald Suite", {
    x: 2, y: 1.8, w: 6, h: 0.8,
    fontSize: 32, bold: true, color: COLORS.textTitle, align: "center", fontFace: "Outfit"
});
s6.addText("Book your seamless, peaceful lakeside getaway today.", {
    x: 2.5, y: 2.6, w: 5, h: 0.6,
    fontSize: 16, color: COLORS.textBody, align: "center", fontFace: "Outfit"
});

// "Button"
s6.addShape(pres.shapes.RECTANGLE, {
    x: 3.5, y: 3.3, w: 3, h: 0.5,
    fill: { color: COLORS.magenta },
    shadow: { type: "outer", color: "000000", blur: 5, offset: 2, angle: 90, opacity: 0.3 }
});
s6.addText("Reserve on Airbnb", {
    x: 3.5, y: 3.3, w: 3, h: 0.5,
    fontSize: 16, bold: true, color: "FFFFFF", align: "center", fontFace: "Outfit"
});

pres.writeFile({ fileName: "EmeraldSuite_Marketing.pptx" }).then(() => {
    console.log("created EmeraldSuite_Marketing.pptx");
});
