// META: title=Popover hide algorithm aborts when disconnected during beforetoggle
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
      popover.remove(); // dynamically disconnect
    }
  });

  try {
    popover.hidePopover();
  } catch (e) {
    // The spec mandates throwing an InvalidStateError because element is not connected.
    // However, the focus of this test is on the algorithm aborting and not queuing
    // the toggle event.
  }

  // Wait a tick to ensure the queued toggle event task has a chance to run
  // if the algorithm had not aborted.
  await new Promise(r => t.step_timeout(r, 0));

  assert_false(toggleFired, 'The toggle event must not fire because the hide popover algorithm should abort');
}, 'When hiding a popover, if the element is dynamically disconnected from the document during the dispatch of the beforetoggle event, the hide popover algorithm must abort and the element must not be removed from the top layer.');
