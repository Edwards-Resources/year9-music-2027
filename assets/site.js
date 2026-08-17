/* The Plot: the only script on the site, and it does one thing.

   Every listen row is built as a plain link to the recording, so with
   scripting off the page still gets a student to the track. This upgrades the
   link into a player that unfolds inside the row, which keeps the block a list
   of works rather than a stack of video frames, and keeps the page from
   talking to the host at all until someone presses play.

   No framework, no build step, no dependency. Same reason the build script has
   none: nobody is going to be in a session when this breaks.

   The `at` argument is how the guide block's cue times will drive this: a cue
   is a second into a named recording, and seeking is done by remounting the
   frame with ?start=, because that needs no player API and so no third-party
   script on the page. */
(function () {
  "use strict";

  var HOST = "https://www.youtube-nocookie.com/embed/";

  function close(row) {
    var frame = row.querySelector(".frame");
    if (frame) frame.parentNode.removeChild(frame);
    var a = row.querySelector(".play");
    if (a) a.setAttribute("aria-expanded", "false");
  }

  function mount(a, at) {
    var row = a.closest(".tr");
    var list = a.closest(".listen");
    // One player at a time in a block. Two tracks playing over each other in a
    // classroom is the whole room's problem, not one student's.
    if (list) {
      Array.prototype.forEach.call(list.querySelectorAll(".tr"), function (r) {
        if (r !== row) close(r);
      });
    }
    var frame = document.createElement("div");
    frame.className = "frame";
    var f = document.createElement("iframe");
    f.src = HOST + a.getAttribute("data-yt") + "?autoplay=1" +
            (at ? "&start=" + at : "");
    f.title = a.getAttribute("data-work") || "Recording";
    f.allow = "accelerometer; clipboard-write; encrypted-media; picture-in-picture";
    f.setAttribute("allowfullscreen", "");
    frame.appendChild(f);
    row.appendChild(frame);
    a.setAttribute("aria-expanded", "true");
  }

  Array.prototype.forEach.call(document.querySelectorAll(".listen .play"), function (a) {
    // Only now is it a toggle rather than a link out, so only now does it say so.
    a.setAttribute("aria-expanded", "false");
    a.addEventListener("click", function (ev) {
      if (ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.button !== 0) return;
      ev.preventDefault();
      var row = a.closest(".tr");
      if (a.getAttribute("aria-expanded") === "true") close(row);
      else mount(a, 0);
    });
  });
})();
