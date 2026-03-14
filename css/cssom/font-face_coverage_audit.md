<status>TESTS_NEEDED</status>
<audit_worksheet>
[Existence]
R1: The `@font-face` rule must be considered invalid if it does not contain a `font-family` descriptor. -> [UNCOVERED]
R2: The `@font-face` rule must be considered invalid if it does not contain a `src` descriptor. -> [UNCOVERED]
R3: The `@font-face` rule must support the `font-size` descriptor. -> [UNCOVERED]
R4: The `@font-face` rule must support the `size-adjust` descriptor. -> [COVERED by font-face-size-adjust.html]
R5: The `@font-face` rule must support the `ascent-override` descriptor. -> [COVERED by font-face-unicode-range-nbsp.html]
R6: The `@font-face` rule must support the `descent-override` descriptor. -> [COVERED by font-face-unicode-range-nbsp.html]
R7: The `@font-face` rule must support the `line-gap-override` descriptor. -> [UNCOVERED]
R8: The `@font-face` rule must support the `superscript-position-override` descriptor. -> [UNCOVERED]
R9: The `@font-face` rule must support the `subscript-position-override` descriptor. -> [UNCOVERED]
R10: The `@font-face` rule must support the `superscript-size-override` descriptor. -> [UNCOVERED]
R11: The `@font-face` rule must support the `subscript-size-override` descriptor. -> [UNCOVERED]
R12: The `CSSFontFaceRule` interface must be exposed on the `Window` object. -> [COVERED by idlharness.html]
R13: The `CSSFontFaceRule` interface must inherit from the `CSSRule` interface. -> [COVERED by idlharness.html]
R14: The `CSSFontFaceRule` interface must contain a readonly `style` attribute of type `CSSFontFaceDescriptors`. -> [COVERED by idlharness.html]
R15: The `CSSFontFaceDescriptors` interface must be exposed on the `Window` object. -> [COVERED by idlharness.html]
R16: The `CSSFontFaceDescriptors` interface must inherit from the `CSSStyleDeclaration` interface. -> [COVERED by idlharness.html]
R17: The `CSSFontFaceDescriptors` interface must contain a `src` attribute of type `CSSOMString`. -> [COVERED by idlharness.html]
R18: The `CSSFontFaceDescriptors` interface must contain `fontFamily` and `font-family` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]
R19: The `CSSFontFaceDescriptors` interface must contain `fontStyle` and `font-style` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]
R20: The `CSSFontFaceDescriptors` interface must contain `fontWeight` and `font-weight` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]
R21: The `CSSFontFaceDescriptors` interface must contain `fontStretch` and `font-stretch` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]
R22: The `CSSFontFaceDescriptors` interface must contain `fontWidth` and `font-width` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]
R23: The `CSSFontFaceDescriptors` interface must contain `fontSize` and `font-size` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]
R24: The `CSSFontFaceDescriptors` interface must contain `sizeAdjust` and `size-adjust` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]
R25: The `CSSFontFaceDescriptors` interface must contain `unicodeRange` and `unicode-range` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]
R26: The `CSSFontFaceDescriptors` interface must contain `fontFeatureSettings` and `font-feature-settings` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]
R27: The `CSSFontFaceDescriptors` interface must contain `fontVariationSettings` and `font-variation-settings` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]
R28: The `CSSFontFaceDescriptors` interface must contain `fontNamedInstance` and `font-named-instance` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]
R29: The `CSSFontFaceDescriptors` interface must contain `fontDisplay` and `font-display` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]
R30: The `CSSFontFaceDescriptors` interface must contain `fontLanguageOverride` and `font-language-override` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]
[Existence]
R31: The `CSSFontFaceDescriptors` interface must contain `ascentOverride` and `ascent-override` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]
R32: The `CSSFontFaceDescriptors` interface must contain `descentOverride` and `descent-override` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]
R33: The `CSSFontFaceDescriptors` interface must contain `lineGapOverride` and `line-gap-override` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]
R34: The `CSSFontFaceDescriptors` interface must contain `superscriptPositionOverride` and `superscript-position-override` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]
R35: The `CSSFontFaceDescriptors` interface must contain `subscriptPositionOverride` and `subscript-position-override` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]
R36: The `CSSFontFaceDescriptors` interface must contain `superscriptSizeOverride` and `superscript-size-override` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]
R37: The `CSSFontFaceDescriptors` interface must contain `subscriptSizeOverride` and `subscript-size-override` attributes of type `CSSOMString`. -> [COVERED by idlharness.html]

[Common Use Cases]
R38: The `@font-face` `src` descriptor value must be parsed as a comma-separated list of component values. -> [COVERED by parsing/font-face-src-list.html]
R39: Each component value in the `@font-face` `src` descriptor must be parsed according to the grammar: `<url> [ format(<font-format>)]? [ tech( <font-tech>#)]? | local(<family-name>)`. -> [COVERED by parsing/font-face-src-format.html]
R40: If a component value in the `src` descriptor is parsed correctly and specifies a supported font format and font tech, it must be added to the list of supported sources. -> [COVERED by parsing/font-face-src-tech.html]
R41: If a component value in the `src` descriptor results in a parsing error, or if its specified format or tech is unsupported, it must not be added to the list of supported sources. -> [COVERED by parsing/font-face-src-tech.html]
R42: If there are no supported entries at the end of parsing the `src` descriptor, the value for the `src` descriptor must be evaluated as a parse error. -> [COVERED by parsing/font-face-src-list.html]
R43: The `size-adjust` descriptor must scale all metrics associated with the font (including glyph advances, baseline tables, and overrides) and the rendered glyph images by the specified percentage. -> [UNCOVERED]
R44: The `size-adjust` descriptor must scale values derived from font metrics, such as `ex` and `ch` units, when sourced from the adjusted font. -> [UNCOVERED]
R45: The `size-adjust` descriptor must not affect the computed `font-size` or any values that derive from it, such as `em` units. -> [UNCOVERED]
R46: When `ascent-override`, `descent-override`, or `line-gap-override` is set to a `<percentage>`, the corresponding metric must be replaced by the specified percentage multiplied by the effective font size after adjustment. -> [UNCOVERED]
R47: The `ascent-override`, `descent-override`, and `line-gap-override` descriptors must not affect the computation of `font-size`, `line-height`, or font-relative lengths. -> [UNCOVERED]
R48: When `superscript-position-override`, `subscript-position-override`, `superscript-size-override`, or `subscript-size-override` is set to a `<percentage>`, the corresponding metric must be replaced by the specified percentage multiplied by the used font size. -> [UNCOVERED]
R49: When `superscript-position-override`, `subscript-position-override`, `superscript-size-override`, or `subscript-size-override` is set to `from-font`, the corresponding metric in the font data must be used. -> [UNCOVERED]
R50: The `font-size-adjust` property must be applied after the `size-adjust` descriptor. -> [UNCOVERED]

[Error Scenarios]
R51: If parsing a component value of the @font-face src descriptor results in a parsing error, the user agent must not add it to the list of supported sources. -> [COVERED by parsing/font-face-src-list.html]
R52: If a component value of the @font-face src descriptor specifies an unsupported format or tech, the user agent must not add it to the list of supported sources. -> [COVERED by parsing/font-face-src-tech.html]
R53: If there are no supported entries remaining after parsing all component values of the @font-face src descriptor, the user agent must treat the value for the src descriptor as a parse error. -> [COVERED by parsing/font-face-src-list.html]
R54: If the font-family descriptor is omitted, the @font-face rule must be considered invalid. -> [UNCOVERED]
R55: If the src descriptor is omitted, the @font-face rule must be considered invalid. -> [UNCOVERED]
R56: If an @font-face rule is declared nested within a CSS selector, it must be treated as invalid. -> [UNCOVERED]

[Integration]
R57: The `@font-face` `src` descriptor value must be parsed according to the 'Parse a comma-separated list of component values' rules defined in CSS Syntax 3. -> [COVERED by parsing/font-face-src-list.html]
R58: When the `size-adjust` descriptor is applied to a `@font-face`, any values derived from font metrics, such as `ex` and `ch` units or the `from-font` value of `text-decoration-thickness`, must be scaled by the given percentage. -> [UNCOVERED]
R59: When both the `font-size-adjust` property and the `@font-face` `size-adjust` descriptor are used, the `font-size-adjust` property must be applied after the `size-adjust` descriptor. -> [UNCOVERED]
R60: The `superscript-position-override`, `subscript-position-override`, `superscript-size-override`, and `subscript-size-override` descriptors must be used to synthesize glyphs when required by the `font-variant-position` property. -> [UNCOVERED]
</audit_worksheet>
<test_suggestions>
<test_suggestion>
    <title>Invalid @font-face without font-family</title>
    <description>The `@font-face` rule must be considered invalid if it does not contain a `font-family` descriptor.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[HTML body with a <style id="testStyle"></style> element]]></pre_conditions>
    <steps>
      <step>1. Insert a `@font-face` rule into the stylesheet with a `src` descriptor but no `font-family` descriptor.</step>
      <step>2. Attempt to use the font in the document and verify it falls back to the next available font.</step>
      <step>3. Check the CSSOM to see if the rule is considered invalid or dropped.</step>
    </steps>
    <expected_result>The rule should be considered invalid and not applied to the document.</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>Invalid @font-face without src</title>
    <description>The `@font-face` rule must be considered invalid if it does not contain a `src` descriptor.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[HTML body with a <style id="testStyle"></style> element]]></pre_conditions>
    <steps>
      <step>1. Insert a `@font-face` rule into the stylesheet with a `font-family` descriptor but no `src` descriptor.</step>
      <step>2. Attempt to use the font in the document and verify it falls back to the next available font.</step>
      <step>3. Check the CSSOM to see if the rule is considered invalid or dropped.</step>
    </steps>
    <expected_result>The rule should be considered invalid and not applied to the document.</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>Support for font-size descriptor in @font-face</title>
    <description>The `@font-face` rule must support the `font-size` descriptor.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[HTML body with a <style id="testStyle"></style> element]]></pre_conditions>
    <steps>
      <step>1. Insert a `@font-face` rule with a `font-size` descriptor.</step>
      <step>2. Read the `getPropertyValue("font-size")` from the rule's style.</step>
    </steps>
    <expected_result>The `font-size` descriptor value should be correctly parsed and returned.</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>Support for line-gap-override descriptor in @font-face</title>
    <description>The `@font-face` rule must support the `line-gap-override` descriptor.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[HTML body with a <style id="testStyle"></style> element]]></pre_conditions>
    <steps>
      <step>1. Insert a `@font-face` rule with a `line-gap-override` descriptor.</step>
      <step>2. Read the `getPropertyValue("line-gap-override")` from the rule's style.</step>
    </steps>
    <expected_result>The `line-gap-override` descriptor value should be correctly parsed and returned.</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>Support for superscript-position-override descriptor in @font-face</title>
    <description>The `@font-face` rule must support the `superscript-position-override` descriptor.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[HTML body with a <style id="testStyle"></style> element]]></pre_conditions>
    <steps>
      <step>1. Insert a `@font-face` rule with a `superscript-position-override` descriptor.</step>
      <step>2. Read the `getPropertyValue("superscript-position-override")` from the rule's style.</step>
    </steps>
    <expected_result>The `superscript-position-override` descriptor value should be correctly parsed and returned.</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>Support for subscript-position-override descriptor in @font-face</title>
    <description>The `@font-face` rule must support the `subscript-position-override` descriptor.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[HTML body with a <style id="testStyle"></style> element]]></pre_conditions>
    <steps>
      <step>1. Insert a `@font-face` rule with a `subscript-position-override` descriptor.</step>
      <step>2. Read the `getPropertyValue("subscript-position-override")` from the rule's style.</step>
    </steps>
    <expected_result>The `subscript-position-override` descriptor value should be correctly parsed and returned.</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>Support for superscript-size-override descriptor in @font-face</title>
    <description>The `@font-face` rule must support the `superscript-size-override` descriptor.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[HTML body with a <style id="testStyle"></style> element]]></pre_conditions>
    <steps>
      <step>1. Insert a `@font-face` rule with a `superscript-size-override` descriptor.</step>
      <step>2. Read the `getPropertyValue("superscript-size-override")` from the rule's style.</step>
    </steps>
    <expected_result>The `superscript-size-override` descriptor value should be correctly parsed and returned.</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>Support for subscript-size-override descriptor in @font-face</title>
    <description>The `@font-face` rule must support the `subscript-size-override` descriptor.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[HTML body with a <style id="testStyle"></style> element]]></pre_conditions>
    <steps>
      <step>1. Insert a `@font-face` rule with a `subscript-size-override` descriptor.</step>
      <step>2. Read the `getPropertyValue("subscript-size-override")` from the rule's style.</step>
    </steps>
    <expected_result>The `subscript-size-override` descriptor value should be correctly parsed and returned.</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>size-adjust scales font metrics and glyphs</title>
    <description>The `size-adjust` descriptor must scale all metrics associated with the font (including glyph advances, baseline tables, and overrides) and the rendered glyph images by the specified percentage.</description>
    <test_type>Reftest</test_type>
    <pre_conditions><![CDATA[HTML body with two divs, one using a normal font, one using a font with size-adjust: 50% and font-size: 200%]]></pre_conditions>
    <steps>
      <step>1. Render text in both divs.</step>
      <step>2. Compare the rendered output.</step>
    </steps>
    <expected_result>The rendered text in both divs should match exactly in size and metrics.</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>size-adjust scales ex and ch units</title>
    <description>The `size-adjust` descriptor must scale values derived from font metrics, such as `ex` and `ch` units, when sourced from the adjusted font.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[HTML body with a div using a font with size-adjust: 50%]]></pre_conditions>
    <steps>
      <step>1. Create a child element with width: 10ch and height: 10ex.</step>
      <step>2. Measure the computed width and height in pixels.</step>
    </steps>
    <expected_result>The computed width and height should be exactly half of what they would be without size-adjust.</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>size-adjust does not affect em units or computed font-size</title>
    <description>The `size-adjust` descriptor must not affect the computed `font-size` or any values that derive from it, such as `em` units.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[HTML body with a div using a font with size-adjust: 50% and font-size: 20px]]></pre_conditions>
    <steps>
      <step>1. Create a child element with width: 10em.</step>
      <step>2. Measure the computed font-size and width.</step>
    </steps>
    <expected_result>The computed font-size should be 20px and the width should be 200px.</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>ascent-override, descent-override, line-gap-override replace metrics</title>
    <description>When `ascent-override`, `descent-override`, or `line-gap-override` is set to a `<percentage>`, the corresponding metric must be replaced by the specified percentage multiplied by the effective font size after adjustment.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[HTML body with a div using a font with ascent-override: 80%, descent-override: 20%, line-gap-override: 10%]]></pre_conditions>
    <steps>
      <step>1. Measure the height of the line box.</step>
    </steps>
    <expected_result>The line box height should reflect the overridden metrics.</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>ascent-override, descent-override, line-gap-override do not affect font-size or em units</title>
    <description>The `ascent-override`, `descent-override`, and `line-gap-override` descriptors must not affect the computation of `font-size`, `line-height`, or font-relative lengths.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[HTML body with a div using a font with ascent-override: 200% and font-size: 20px]]></pre_conditions>
    <steps>
      <step>1. Create a child element with width: 10em.</step>
      <step>2. Measure the computed font-size and width.</step>
    </steps>
    <expected_result>The computed font-size should be 20px and the width should be 200px.</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>superscript and subscript overrides with percentage</title>
    <description>When `superscript-position-override`, `subscript-position-override`, `superscript-size-override`, or `subscript-size-override` is set to a `<percentage>`, the corresponding metric must be replaced by the specified percentage multiplied by the used font size.</description>
    <test_type>Reftest</test_type>
    <pre_conditions><![CDATA[HTML body with a div using a font with superscript-position-override: 50%]]></pre_conditions>
    <steps>
      <step>1. Render text with font-variant-position: super.</step>
    </steps>
    <expected_result>The superscript glyphs should be positioned according to the 50% override.</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>superscript and subscript overrides with from-font</title>
    <description>When `superscript-position-override`, `subscript-position-override`, `superscript-size-override`, or `subscript-size-override` is set to `from-font`, the corresponding metric in the font data must be used.</description>
    <test_type>Reftest</test_type>
    <pre_conditions><![CDATA[HTML body with a div using a font with superscript-position-override: from-font]]></pre_conditions>
    <steps>
      <step>1. Render text with font-variant-position: super.</step>
    </steps>
    <expected_result>The superscript glyphs should be positioned according to the font's internal metrics.</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>font-size-adjust applied after size-adjust</title>
    <description>The `font-size-adjust` property must be applied after the `size-adjust` descriptor.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[HTML body with a div using a font with size-adjust: 50% and font-size-adjust: 0.5]]></pre_conditions>
    <steps>
      <step>1. Measure the computed ex height or actual rendered glyph size.</step>
    </steps>
    <expected_result>The final size should reflect font-size-adjust applied on top of the size-adjust scaled metrics.</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>@font-face without font-family is invalid</title>
    <description>If the font-family descriptor is omitted, the @font-face rule must be considered invalid.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[None]]></pre_conditions>
    <steps>
      <step>1. Insert a stylesheet with `@font-face { src: url(font.ttf); }`.</step>
      <step>2. Check document.styleSheets[0].cssRules.</step>
    </steps>
    <expected_result>The rule should not be parsed or should be considered invalid (cssRules.length === 0).</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>@font-face without src is invalid</title>
    <description>If the src descriptor is omitted, the @font-face rule must be considered invalid.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[None]]></pre_conditions>
    <steps>
      <step>1. Insert a stylesheet with `@font-face { font-family: 'Test'; }`.</step>
      <step>2. Check document.styleSheets[0].cssRules.</step>
    </steps>
    <expected_result>The rule should not be parsed or should be considered invalid (cssRules.length === 0).</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>Nested @font-face is invalid</title>
    <description>If an @font-face rule is declared nested within a CSS selector, it must be treated as invalid.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[None]]></pre_conditions>
    <steps>
      <step>1. Insert a stylesheet with `div { @font-face { font-family: 'Test'; src: url(font.ttf); } }`.</step>
      <step>2. Check document.styleSheets[0].cssRules.</step>
    </steps>
    <expected_result>The nested @font-face rule should be dropped or treated as invalid.</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>size-adjust scales ex, ch, and text-decoration-thickness</title>
    <description>When the `size-adjust` descriptor is applied to a `@font-face`, any values derived from font metrics, such as `ex` and `ch` units or the `from-font` value of `text-decoration-thickness`, must be scaled by the given percentage.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[HTML body with a div using a font with size-adjust: 50%]]></pre_conditions>
    <steps>
      <step>1. Measure computed values of 1ex, 1ch, and text-decoration-thickness: from-font.</step>
    </steps>
    <expected_result>The computed values should be scaled by 50%.</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>font-size-adjust applied after size-adjust (Integration)</title>
    <description>When both the `font-size-adjust` property and the `@font-face` `size-adjust` descriptor are used, the `font-size-adjust` property must be applied after the `size-adjust` descriptor.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[HTML body with a div using a font with size-adjust: 50% and font-size-adjust: 0.5]]></pre_conditions>
    <steps>
      <step>1. Measure the computed ex height.</step>
    </steps>
    <expected_result>The final size should reflect font-size-adjust applied on top of the size-adjust scaled metrics.</expected_result>
  </test_suggestion>
<test_suggestion>
    <title>superscript and subscript overrides synthesize glyphs</title>
    <description>The `superscript-position-override`, `subscript-position-override`, `superscript-size-override`, and `subscript-size-override` descriptors must be used to synthesize glyphs when required by the `font-variant-position` property.</description>
    <test_type>Reftest</test_type>
    <pre_conditions><![CDATA[HTML body with a div using a font with superscript-position-override: 50% and font-variant-position: super]]></pre_conditions>
    <steps>
      <step>1. Render text.</step>
    </steps>
    <expected_result>The text should be rendered with synthesized superscript glyphs using the overridden metrics.</expected_result>
  </test_suggestion>
</test_suggestions>
