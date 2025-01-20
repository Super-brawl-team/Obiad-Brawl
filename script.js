var base = Module.findBaseAddress('Brawl Stars');
function startGrab() {
Interceptor.attach(base.add(0x9F708), {
  onEnter: function(args) {
        this.arg2 = args[1].toInt32(); // Store the value of args[2]
    },
    onLeave: function(retval) {
        console.log("self.writePositiveInt(" + retval.toUInt32() + ", " + this.arg2 + ")");
    }
});
Interceptor.attach(base.add(0x9F7D0), {
    onEnter: function(args) {
         console.log("self.writePositiveInt(" + args[1].toInt32() + "," + args[2].toInt32() + ")")
   },
});
}

Interceptor.attach(base.add(0x39830), {
  onEnter: function(args) {
        startGrab()
    },
    onLeave: function(retval) {
      Interceptor.detachAll()
    }
});
//Interceptor.attach(base.add(0x9F7D0), {
  //  onEnter: function(args) {
    //     console.log("self.writePositiveInt(" + args[2].toInt32 + ")")
//   },
//});