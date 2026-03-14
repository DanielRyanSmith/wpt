<audit_worksheet>
[Existence]
R1: The `will-change` CSS property must be supported and apply to all elements. -> [COVERED by parsing/will-change-valid.html]
R2: The initial value of the `will-change` property must be `auto`. -> [COVERED by inheritance.html]
R3: The `will-change` property must not be inherited. -> [COVERED by inheritance.html]
R4: The computed value of the `will-change` property must be its specified value. -> [COVERED by parsing/will-change-computed.html]
R5: The `will-change` property must not be animatable. -> [UNCOVERED]
R6: The `will-change` property must accept the keyword `auto`. -> [COVERED by parsing/will-change-valid.html]
R7: The `will-change` property must accept a comma-separated list of one or more `<animateable-feature>` values, which consist of `scroll-position`, `contents`, or a `<custom-ident>`. -> [COVERED by parsing/will-change-valid.html]
R8: When parsing a `<custom-ident>` value for the `will-change` property, the keywords `will-change`, `none`, `all`, `auto`, `scroll-position`, and `contents` must be excluded and treated as invalid. -> [COVERED by parsing/will-change-invalid.html]
R9: When parsing a `<custom-ident>` value for the `will-change` property, the value must be matched ASCII case-insensitively against the names of built-in CSS properties. -> [COVERED by parsing/will-change-valid.html]

[Common Use Cases]
R10: When parsing the `will-change` property, a `<custom-ident>` value must be considered invalid if it is an ASCII case-insensitive match for the keywords `will-change`, `none`, `all`, `auto`, `scroll-position`, or `contents`. -> [UNCOVERED]
R11: If a custom CSS property is specified as a `<custom-ident>` value in the `will-change` property, it must have no effect. -> [UNCOVERED]
R12: If any non-initial value of a CSS property would create a stacking context on the element, specifying that property in `will-change` must create a stacking context on the element. -> [COVERED by will-change-stacking-context-opacity-1.html]
R13: If any non-initial value of a CSS property would cause the element to generate a containing block for absolutely positioned elements, specifying that property in `will-change` must cause the element to generate a containing block for absolutely positioned elements. -> [COVERED by will-change-abspos-cb-001.html]
R14: If any non-initial value of a CSS property would cause the element to generate a containing block for fixed positioned elements, specifying that property in `will-change` must cause the element to generate a containing block for fixed positioned elements. -> [COVERED by will-change-fixpos-cb-transform-1.html]

[Error Scenarios]
R15: The keywords 'will-change', 'none', 'all', 'auto', 'scroll-position', and 'contents' must be excluded from the <custom-ident> production, rendering the declaration invalid if they are used as custom identifiers. -> [COVERED by parsing/will-change-invalid.html]

[Integration]
R16: If a custom property is specified in the will-change property, it must have no effect and must not trigger the creation of stacking contexts or containing blocks. -> [UNCOVERED]
R17: If specifying any non-initial value of a CSS property would create a stacking context on an element, specifying that property in will-change must create a stacking context on the element. -> [COVERED by will-change-stacking-context-opacity-1.html]
R18: If specifying any non-initial value of a CSS property would cause an element to generate a containing block for absolutely positioned elements, specifying that property in will-change must cause the element to generate a containing block for absolutely positioned elements. -> [COVERED by will-change-abspos-cb-001.html]
R19: If specifying any non-initial value of a CSS property would cause an element to generate a containing block for fixed positioned elements, specifying that property in will-change must cause the element to generate a containing block for fixed positioned elements. -> [COVERED by will-change-fixpos-cb-transform-1.html]
</audit_worksheet>

<test_suggestions>
  <test_suggestion>
    <title>will-change invalid custom-ident case-insensitivity</title>
    <description>When parsing the `will-change` property, a `<custom-ident>` value must be considered invalid if it is an ASCII case-insensitive match for the keywords `will-change`, `none`, `all`, `auto`, `scroll-position`, or `contents`.</description>
    <test_type>JavaScript test</test_type>
    <pre_conditions><![CDATA[None]]></pre_conditions>
    <steps>
      <step>1. Evaluate CSS.supports("will-change", "NONE").</step>
      <step>2. Evaluate CSS.supports("will-change", "ALL").</step>
      <step>3. Evaluate CSS.supports("will-change", "WILL-CHANGE").</step>
      <step>4. Evaluate CSS.supports("will-change", "AUTO, transform").</step>
    </steps>
    <expected_result>All CSS.supports calls should return false.</expected_result>
  </test_suggestion>
  <test_suggestion>
    <title>will-change custom property has no effect</title>
    <description>If a custom CSS property is specified as a `<custom-ident>` value in the `will-change` property, it must have no effect.</description>
    <test_type>Reftest</test_type>
    <pre_conditions><![CDATA[HTML body with a container div and two child divs (one positioned absolute with negative z-index, one static).]]></pre_conditions>
    <steps>
      <step>1. Apply `will-change: --my-custom-property` to the container.</step>
      <step>2. Position the first child absolutely with `z-index: -1` and a green background.</step>
      <step>3. Give the container a red background.</step>
    </steps>
    <expected_result>The container should not create a stacking context, so the green child should render behind the red container (or body background), matching a reference without will-change.</expected_result>
  </test_suggestion>
  <test_suggestion>
    <title>will-change custom property does not create containing block</title>
    <description>If a custom property is specified in the will-change property, it must have no effect and must not trigger the creation of stacking contexts or containing blocks.</description>
    <test_type>Reftest</test_type>
    <pre_conditions><![CDATA[HTML body with a container div and an absolutely positioned child div.]]></pre_conditions>
    <steps>
      <step>1. Apply `will-change: --my-custom-property` to the container.</step>
      <step>2. Apply `margin-top: 100px; margin-left: 100px;` to the container.</step>
      <step>3. Apply `position: absolute; top: 0; left: 0;` to the child.</step>
    </steps>
    <expected_result>The child should be positioned relative to the initial containing block (viewport), not the container, appearing at the top-left of the page.</expected_result>
  </test_suggestion>
</test_suggestions>