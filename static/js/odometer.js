function Scroller(opts) {
  this.opts = opts || {};

  this.start = function() {
    $(_this.opts.selector).each(function() {
      var $this = $(this);
      var height = $this.height();
      var text = $this.text();
      var numText = text.match(/\d/gi).join('');
      var newText = '';

      $this.addClass('scroller-wrapper');

      for (var i = 0; i <= numText.length; i += 1) {
        if (!numText[i]) continue;

        var range = '';
        var style = '';
        var num = parseInt(numText[i], 10);
        var dur = Math.ceil(num / numText.length);
        // Create the full range (0 - num)
        for (var j = 0; j <= num ; j += 1) {
          range += wrap(j, 'span');
        }

        // Create the styling
        style += 'animation-duration: ' + dur + 's;';
        style += 'animation-timing-function: ease-out;';
        style += 'animation-name: scroller-' + num + ';';
        // Final HTML
        newText += wrap(range, 'div', style);

        // Restore
        setTimeout(function (i) {
          $this.html(text);
        }.bind(null, i), dur * 1000)
      }
      $this.html(newText).height(height);
    });
  };

  //Helpers
  var _this = this;
  var wrap = function (text, tag, style) {
    var styleAttr = style ? ' style="' + style + '"' : '';
    return '<' + tag + styleAttr + '>' + text + '</' + tag + '>';
  }
}

var scroller = new Scroller({
  selector: ".scroller"
});

setTimeout(function () {
  scroller.start()
}, 1000)
