// META: title=ShadowRoot.fullscreenElement on disconnected host
// https://fullscreen.spec.whatwg.org/

test(() => {
  const host = document.createElement("div");
  const shadow = host.attachShadow({ mode: "open" });
  assert_equals(shadow.fullscreenElement, null);
}, "fullscreenElement accessed on an open shadow root whose host is not connected to the DOM must return null.");

test(() => {
  const host = document.createElement("div");
  const shadow = host.attachShadow({ mode: "closed" });
  assert_equals(shadow.fullscreenElement, null);
}, "fullscreenElement accessed on a closed shadow root whose host is not connected to the DOM must return null.");

test(() => {
  const parent = document.createElement("div");
  const host = document.createElement("div");
  parent.appendChild(host);
  const shadow = host.attachShadow({ mode: "open" });
  assert_equals(shadow.fullscreenElement, null);
}, "fullscreenElement accessed on a shadow root whose host is in a disconnected tree must return null.");
