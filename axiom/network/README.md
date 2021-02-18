# `axiom.network`

The basic interactions and dependencies of this package can be a little confusion, but here it's explained a little
better;

`axiom.network.service.NetworkService` is the "bridge" that holds any sub-dependent services, e.g. `FederationService`
and `ClientServerService`.

These sub-dependent services (called "`XService`" from now on) act as two-way specialized bridges for both the backing
network implementation, and the homeserver. This abstracts the network with explicit bridging methods, on the cost of
name-duplication between network implementation, `XService` implementation, and homeserver implementation.

The network implementation utilizes `XService` as a "telephone" to communicate with the homeserver, and the homeserver
uses `XService` to "telephone" back to the network implementation, this allows relative flexibility between specific
implementations, and allows experimentation.

The `XService`s defines the widest "band" of communication between the network and the server, but this is fine, as this
means that all interaction is made explicit, and any new additions to these `XService`s make any new possible motion of
communication clear.

All `XService`s' methods must have typing, every method providing a passthrough for either network or server must be
explicitly named thus;

- Any method used by the network implementation MUST be prefixed with `net_`
- Any method used by the server implementation MUST be prefixed with `srv_`
- Any method used internally (e.g. to call back to server for additional logic required, or to network to resolve a
  particular piece of data) MUST be prefixed with `_`, with the callee's prefix after that.
- Any method, which for some reason is used by either callee, MUST be prefixed with `any_`, please keep these methods to
  a minimum if possible. *Please* do not call any specific method with this, e.g. `net_` or `srv_`.

### Bootstrapping

Any network implementation must subclass `NetworkService` and all `XService`s.

`NetworkService` subclasses need to be adjusted to point to the subclassed `XService`s, and all `XService`s must meet their
superclass' method signatures, some server-calling `XService` methods might be implemented, but a network implementation is allowed to change it to suit their needs.

`NetworkService` accepts an `MatrixHomeServer` instance as it's first argument, this can/should be used to bootstrap
the `XService`s' with an object reference to the server, to call upon network events.

It is recommended to use this method of bootstrapping, as it allows any kind of abstract server logic to coincide with
abstract network logic. Ultimately, it is also recommended letting the server do the instantiating of
the `NetworkService`, this sets the dependency relationship where the server is "above" the network, and the network can
only communicate with the server through the relevant `XService`s.

### Abstraction Co-dependency

The co-dependency of any `XService` is with `MatrixHomeServer`, in the form of `XService` methods calling method
signatures declared on `MatrixHomeServer`.

Take extra care when removing signatures from `MatrixHomeServer`, as a method in any `XService` could depend on it.

Take extra care when adding or removing signatures from `XService`s. Removing signatures might break calls from any
network implementations calling towards a server with it, as well as any server implementation calling towards the
network. Adding signatures might raise errors in existing network implementations, as these signatures would not be
implemented in their corresponding `XService` subclasses.
