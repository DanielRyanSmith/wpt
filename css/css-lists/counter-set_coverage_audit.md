<audit_worksheet>
[Existence]
R1: The `counter-set` property must accept the keyword `none` as a valid value. -> [COVERED by counter-set-valid.html]
R2: The `counter-set` property must accept a list of one or more `<counter-name>` identifiers, each optionally followed by an `<integer>`. -> [COVERED by counter-set-valid.html]
R3: The `counter-set` property must reject the keyword `none` when used as a `<counter-name>` identifier. -> [COVERED by counter-set-invalid.html]
R4: The initial value of the `counter-set` property must be `none`. -> [UNCOVERED]
R5: The `counter-set` property must apply to all elements. -> [UNCOVERED]
R6: The `counter-set` property must not be inherited. -> [UNCOVERED]
R7: The computed value of the `counter-set` property must be the keyword `none` or a list where each item is an identifier paired with an integer. -> [COVERED by counter-set-computed.html]

[Common Use Cases]
R8: If the `counter-set` property is set to `none`, the element must not alter the value of any counters. -> [UNCOVERED]
R9: If the `counter-set` property specifies a counter name and an integer, it must set the value of the named counter on the element to the specified integer. -> [COVERED by counter-set-001.html]
R10: If the `counter-set` property specifies a counter name but the integer value is omitted, the integer value must default to 0. -> [COVERED by counter-set-001.html]
R11: If the `counter-set` property specifies a counter name that does not currently exist on the element, the element must instantiate a new counter of the given name with a starting value of 0 before setting its value. -> [COVERED by counter-set-001.html]
R12: If multiple instances of the same counter name occur in the `counter-set` property value, they must be processed in order such that only the last set value takes effect. -> [COVERED by counter-set-001.html]
R13: If the `counter-set` property is applied to an element that does not generate a box (such as an element with `display: none`), the property must have no effect on the counter. -> [UNCOVERED]

[Error Scenarios]
R14: If the counter name provided to the counter-set property is the keyword 'none', it must be treated as an invalid identifier. -> [COVERED by counter-set-invalid.html]
R15: If the counter-set property is applied to an element that does not generate a box (such as an element with display: none), the property must have no effect. -> [UNCOVERED]
R16: If the counter-set property specifies a value that pushes the counter outside the implementation-specific maximum or minimum range, the value must be clamped to that range. -> [UNCOVERED]

[Integration]
R17: If an element does not generate a box (such as an element with the display property set to none, or a pseudo-element with the content property set to none), the counter-set property must have no effect on the counter values. -> [UNCOVERED]
</audit_worksheet>

<test_suggestions>
  <test_suggestion>
    <title>counter-set initial value</title>
    <description>The initial value of the `counter-set` property must be `none`.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[HTML body with <div id='target'></div>]]></pre_conditions>
    <steps>
      <step>1. Get the computed style of the target element.</step>
      <step>2. Read the value of the 'counter-set' property.</step>
    </steps>
    <expected_result>The computed value is 'none'.</expected_result>
  </test_suggestion>

  <test_suggestion>
    <title>counter-set applies to all elements</title>
    <description>The `counter-set` property must apply to all elements.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[HTML body with various elements (e.g., <div>, <span>, <svg>, <math>)]]></pre_conditions>
    <steps>
      <step>1. Apply 'counter-set: my-counter 5' to each element.</step>
      <step>2. Get the computed style of each element.</step>
    </steps>
    <expected_result>The 'counter-set' property computes to 'my-counter 5' for all tested elements.</expected_result>
  </test_suggestion>

  <test_suggestion>
    <title>counter-set is not inherited</title>
    <description>The `counter-set` property must not be inherited.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[HTML body with <div id='parent'><div id='child'></div></div>]]></pre_conditions>
    <steps>
      <step>1. Apply 'counter-set: my-counter 5' to the parent element.</step>
      <step>2. Get the computed style of the child element.</step>
    </steps>
    <expected_result>The 'counter-set' property computes to 'none' for the child element.</expected_result>
  </test_suggestion>

  <test_suggestion>
    <title>counter-set: none does not alter counters</title>
    <description>If the `counter-set` property is set to `none`, the element must not alter the value of any counters.</description>
    <test_type>Reftest</test_type>
    <pre_conditions><![CDATA[HTML body with a counter initialized to 1.]]></pre_conditions>
    <steps>
      <step>1. Create an element with 'counter-set: none'.</step>
      <step>2. Create a subsequent element that displays the counter value using a pseudo-element.</step>
    </steps>
    <expected_result>The counter value displayed is 1, not reset or altered.</expected_result>
  </test_suggestion>

  <test_suggestion>
    <title>counter-set on display: none element</title>
    <description>If the `counter-set` property is applied to an element that does not generate a box (such as an element with `display: none`), the property must have no effect on the counter.</description>
    <test_type>Reftest</test_type>
    <pre_conditions><![CDATA[HTML body with a counter initialized to 1.]]></pre_conditions>
    <steps>
      <step>1. Create an element with 'display: none' and 'counter-set: my-counter 5'.</step>
      <step>2. Create a subsequent element that displays the counter value.</step>
    </steps>
    <expected_result>The counter value displayed is 1, not 5.</expected_result>
  </test_suggestion>

  <test_suggestion>
    <title>counter-set on display: none element (Error Scenarios)</title>
    <description>If the counter-set property is applied to an element that does not generate a box (such as an element with display: none), the property must have no effect.</description>
    <test_type>Reftest</test_type>
    <pre_conditions><![CDATA[HTML body with a counter initialized to 1.]]></pre_conditions>
    <steps>
      <step>1. Create an element with 'display: none' and 'counter-set: my-counter 5'.</step>
      <step>2. Create a subsequent element that displays the counter value.</step>
    </steps>
    <expected_result>The counter value displayed is 1, not 5.</expected_result>
  </test_suggestion>

  <test_suggestion>
    <title>counter-set value clamping</title>
    <description>If the counter-set property specifies a value that pushes the counter outside the implementation-specific maximum or minimum range, the value must be clamped to that range.</description>
    <test_type>Testharness test</test_type>
    <pre_conditions><![CDATA[HTML body with <div id='target'></div>]]></pre_conditions>
    <steps>
      <step>1. Apply 'counter-set: my-counter 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999' to the target element.</step>
      <step>2. Get the computed style of the target element.</step>
    </steps>
    <expected_result>The integer value is clamped to the implementation-specific maximum range.</expected_result>
  </test_suggestion>

  <test_suggestion>
    <title>counter-set on elements not generating a box</title>
    <description>If an element does not generate a box (such as an element with the display property set to none, or a pseudo-element with the content property set to none), the counter-set property must have no effect on the counter values.</description>
    <test_type>Reftest</test_type>
    <pre_conditions><![CDATA[HTML body with a counter initialized to 1.]]></pre_conditions>
    <steps>
      <step>1. Create an element with a ::before pseudo-element having 'content: none' and 'counter-set: my-counter 5'.</step>
      <step>2. Create a subsequent element that displays the counter value.</step>
    </steps>
    <expected_result>The counter value displayed is 1, not 5.</expected_result>
  </test_suggestion>
</test_suggestions>