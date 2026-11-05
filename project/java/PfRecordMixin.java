package example;

/* metamodel_version: 1.12.0 */
/* version: 2024 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  What every record of the framework has, so that other records can refer to it: an identifier, a title and a description.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PfRecordMixin  {

  private URI pfId;
  private String title;
  private String description;


}