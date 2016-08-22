### MeterToDB
Adds readings from bemasher/rtlamr project into a database for analysis, graphing, etc.

### Requires:  
  * [`github.com/bemasher/rtlamr`](http://github.com/bemasher/rtlamr) and it's dependencies (If you don't have this up and running solidly, then you're going to have a bad time)  
  * Python (Built using 2.7.12, but any recent version should work)  
  * MySQL (might extend to other databases later)  
  
### Usage:  
You'll need 2 terminals for this program, 1 to get the SDR fired up and 1 to do the database work.  
Terminal 1:  `rtl_tcp` gets the radio set up and ready to receive commands  
Terminal 2:  `py MeterToDB` starts the logging program  
