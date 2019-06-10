console.log("Frida started");
var unlinkPtr = Module.findExportByName(null,'unlinkat');
console.log(unlinkPtr);
Interceptor.replace(unlinkPtr, new NativeCallback(function (){ 
    console.log("[*] Intercepted");
   }, 'int', []));
