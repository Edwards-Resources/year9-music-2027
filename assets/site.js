/* The Plot: the only script on the site, and it does one thing.

   Every work is named by a plain link to its recording, so with scripting off
   the page still gets a student to the track, and every cue time is a plain
   link to that recording at that second. This upgrades both into a player that
   unfolds in place, which keeps the listen block a list of works rather than a
   stack of video frames, keeps the cue sheet a sheet, and keeps the page from
   talking to the host at all until someone presses something.

   No framework, no build step, no dependency. Same reason the build script has
   none: nobody is going to be in a session when this breaks.

   Seeking is done by remounting the frame with ?start=, because that needs no
   player API and so no third-party script on the page. It costs a reload on
   each cue, which is the trade: a cue sheet that works with one 60-line file
   against one that pulls in somebody else's API to save a second. */
(function () {
  "use strict";

  var HOST = "https://www.youtube-nocookie.com/embed/";
  // Where a player may open. A listen row and a cue sheet's work are the same
  // thing to this script: a slot with the name of a work at the top of it.
  var SLOT = ".tr, .gw";

  function close(slot) {
    var frame = slot.querySelector(".frame");
    if (frame) frame.parentNode.removeChild(frame);
    var a = slot.querySelector(".play");
    if (a) a.setAttribute("aria-expanded", "false");
  }

  function mount(slot, at) {
    var a = slot.querySelector(".play");
    if (!a) return;
    // One player at a time on the page, not one per block. Two tracks playing
    // over each other in a classroom is the whole room's problem, and it is
    // just as much the room's problem when one is in the cue sheet and the
    // other is in the listen block.
    Array.prototype.forEach.call(document.querySelectorAll(SLOT), function (s) {
      if (s !== slot) close(s);
    });
    close(slot);
    var frame = document.createElement("div");
    frame.className = "frame";
    var f = document.createElement("iframe");
    f.src = HOST + a.getAttribute("data-yt") + "?autoplay=1" +
            (at ? "&start=" + at : "");
    f.title = a.getAttribute("data-work") || "Recording";
    f.allow = "accelerometer; clipboard-write; encrypted-media; picture-in-picture";
    f.setAttribute("allowfullscreen", "");
    frame.appendChild(f);
    // In a cue sheet the player belongs above that work's own cues, so pressing
    // a cue leaves the rest of the list where it was. In a listen row there is
    // nothing below it and it lands at the end.
    var cues = slot.querySelector(".cues");
    if (cues) slot.insertBefore(frame, cues);
    else slot.appendChild(frame);
    a.setAttribute("aria-expanded", "true");
  }

  function plain(ev) {
    return !(ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.button !== 0);
  }

  Array.prototype.forEach.call(document.querySelectorAll(".play"), function (a) {
    // Only now is it a toggle rather than a link out, so only now does it say so.
    a.setAttribute("aria-expanded", "false");
    a.addEventListener("click", function (ev) {
      if (!plain(ev)) return;
      ev.preventDefault();
      var slot = a.closest(SLOT);
      if (a.getAttribute("aria-expanded") === "true") close(slot);
      else mount(slot, 0);
    });
  });

  // A cue always plays from its own time, open or shut. It is never a toggle:
  // pressing 1:04 has one obvious meaning and closing the player is not it.
  Array.prototype.forEach.call(document.querySelectorAll(".cue"), function (a) {
    a.addEventListener("click", function (ev) {
      if (!plain(ev)) return;
      ev.preventDefault();
      mount(a.closest(SLOT), parseInt(a.getAttribute("data-at"), 10) || 0);
    });
  });
})();
