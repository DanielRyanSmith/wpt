// META: script=/resources/testdriver.js
// META: script=/resources/testdriver-vendor.js
// Spec: https://fullscreen.spec.whatwg.org/

const customCleanup = async () => {
  if (document.fullscreenElement) {
    await document.exitFullscreen();
  }
};

const testCases = [
  {
    desc: 'Fullscreen element outside of auto popover',
    setup: (t) => {
      const p1 = document.createElement('div');
      p1.popover = 'auto';
      document.body.appendChild(p1);
      t.add_cleanup(() => p1.remove());

      const fs = document.createElement('div');
      document.body.appendChild(fs);
      t.add_cleanup(() => fs.remove());

      p1.showPopover();
      return { popovers: [{ element: p1, expectOpen: false }], fs };
    }
  },
  {
    desc: 'Fullscreen element outside of manual popover',
    setup: (t) => {
      const p1 = document.createElement('div');
      p1.popover = 'manual';
      document.body.appendChild(p1);
      t.add_cleanup(() => p1.remove());

      const fs = document.createElement('div');
      document.body.appendChild(fs);
      t.add_cleanup(() => fs.remove());

      p1.showPopover();
      return { popovers: [{ element: p1, expectOpen: true }], fs };
    }
  },
  {
    desc: 'Fullscreen element inside of auto popover',
    setup: (t) => {
      const p1 = document.createElement('div');
      p1.popover = 'auto';
      document.body.appendChild(p1);
      t.add_cleanup(() => p1.remove());

      const fs = document.createElement('div');
      p1.appendChild(fs);

      p1.showPopover();
      return { popovers: [{ element: p1, expectOpen: true }], fs };
    }
  },
  {
    desc: 'Fullscreen element inside of manual popover',
    setup: (t) => {
      const p1 = document.createElement('div');
      p1.popover = 'manual';
      document.body.appendChild(p1);
      t.add_cleanup(() => p1.remove());

      const fs = document.createElement('div');
      p1.appendChild(fs);

      p1.showPopover();
      return { popovers: [{ element: p1, expectOpen: true }], fs };
    }
  },
  {
    desc: 'Fullscreen element inside ancestor popover, with sibling auto popover',
    setup: (t) => {
      const p1 = document.createElement('div');
      p1.popover = 'auto';
      document.body.appendChild(p1);
      t.add_cleanup(() => p1.remove());

      const p2 = document.createElement('div');
      p2.popover = 'auto';
      p1.appendChild(p2);

      const fs = document.createElement('div');
      p1.appendChild(fs);

      p1.showPopover();
      p2.showPopover();
      return { popovers: [
        { element: p1, expectOpen: true },
        { element: p2, expectOpen: false }
      ], fs };
    }
  },
  {
    desc: 'Fullscreen element inside ancestor popover, with sibling manual popover',
    setup: (t) => {
      const p1 = document.createElement('div');
      p1.popover = 'auto';
      document.body.appendChild(p1);
      t.add_cleanup(() => p1.remove());

      const p2 = document.createElement('div');
      p2.popover = 'manual';
      p1.appendChild(p2);

      const fs = document.createElement('div');
      p1.appendChild(fs);

      p1.showPopover();
      p2.showPopover();
      return { popovers: [
        { element: p1, expectOpen: true },
        { element: p2, expectOpen: true }
      ], fs };
    }
  },
  {
    desc: 'Fullscreen element inside nested auto popovers',
    setup: (t) => {
      const p1 = document.createElement('div');
      p1.popover = 'auto';
      document.body.appendChild(p1);
      t.add_cleanup(() => p1.remove());

      const p2 = document.createElement('div');
      p2.popover = 'auto';
      p1.appendChild(p2);

      const fs = document.createElement('div');
      p2.appendChild(fs);

      p1.showPopover();
      p2.showPopover();
      return { popovers: [
        { element: p1, expectOpen: true },
        { element: p2, expectOpen: true }
      ], fs };
    }
  }
];

for (const { desc, setup } of testCases) {
  promise_test(async (t) => {
    t.add_cleanup(customCleanup);
    const { popovers, fs } = setup(t);

    for (let i = 0; i < popovers.length; i++) {
      assert_true(popovers[i].element.matches(':popover-open'), `popover ${i + 1} should be initially open`);
    }

    await test_driver.bless("request fullscreen");
    await fs.requestFullscreen();

    for (let i = 0; i < popovers.length; i++) {
      const { element, expectOpen } = popovers[i];
      if (expectOpen) {
        assert_true(element.matches(':popover-open'), `popover ${i + 1} should remain open`);
      } else {
        assert_false(element.matches(':popover-open'), `popover ${i + 1} should be closed`);
      }
    }
  }, desc);
}
