// META: title=Popover hide algorithm aborts when the attribute is dynamically changed to the 'No Popover' state during beforetoggle
// https://html.spec.whatwg.org/multipage/popover.html

promise_test(async t => {
  const popover = document.createElement('div');
  popover.popover = 'auto';
  document.body.appendChild(popover);
  t.add_cleanup(() => popover.remove());

  popover.showPopover();

  let toggleFired = false;
  popover.addEventListener('toggle', () => {
    toggleFired = true;
  });

  popover.addEventListener('beforetoggle', (e) => {
    if (e.newState === 'closed') {
      popover.removeAttribute('popover'); // dynamically change to 'No Popover' state
    }
  });

  try {
    popover.hidePopover();
    assert_unreached('hidePopover() should throw NotSupportedError');
  } catch (e) {
    assert_equals(e.name, 'NotSupportedError');
  }

  // Wait a tick to ensure the queued toggle event task has a chance to run
  // if the algorithm had not aborted.
  await new Promise(r => t.step_timeout(r, 0));

  assert_false(toggleFired, 'The toggle event must not fire because the hide popover algorithm should abort');
}, "When hiding a popover, if the element's `popover` attribute is dynamically changed to the 'No Popover' state during the dispatch of the `beforetoggle` event, the hide popover algorithm must abort and the element must not be removed from the top layer.");
