const TIME_LIMIT = 10000;

module.exports = {

  zoomIn: function(c, proj) {
    c.click(`#wv-map [data-proj='${proj}'] button.wv-map-zoom-in`);
    c.pause(100);
  },

};